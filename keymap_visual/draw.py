#!/usr/bin/env python3

import sys
from html import escape
from itertools import chain
from typing import Literal, Optional, Sequence, Mapping, Union

import yaml
from pydantic import BaseModel, Field, validator, root_validator


KEY_W = 55
KEY_H = 50
KEY_RX = 6
KEY_RY = 6
INNER_PAD_W = 2
INNER_PAD_H = 2
OUTER_PAD_W = KEY_W / 2
OUTER_PAD_H = KEY_H
KEYSPACE_W = KEY_W + 2 * INNER_PAD_W
KEYSPACE_H = KEY_H + 2 * INNER_PAD_H
LINE_SPACING = 18

STYLE = """
    svg {
        font-family: SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;
        font-size: 14px;
        font-kerning: normal;
        text-rendering: optimizeLegibility;
        fill: #24292e;
    }

    rect {
        fill: #f6f8fa;
        stroke: #d6d8da;
        stroke-width: 1;
    }

    .held {
        fill: #fdd;
    }

    .combo {
        fill: #cdf;
    }

    text {
        text-anchor: middle;
        dominant-baseline: middle;
    }

    .label {
        font-weight: bold;
        text-anchor: start;
        stroke: white;
        stroke-width: 2;
        paint-order: stroke;
    }

    .small {
        font-size: 80%;
    }
"""


class Key(BaseModel):
    tap: str
    hold: str = ""
    type: Literal[None, "held", "combo"] = None

    @classmethod
    def from_key_spec(cls, key_spec: Union[str, "Key"]) -> "Key":
        if isinstance(key_spec, str):
            return cls(tap=key_spec)
        return key_spec


class ComboSpec(BaseModel):
    positions: Sequence[int]
    key: Key
    layers: Sequence[str] = []

    @validator("key", pre=True)
    def get_key(cls, val):
        return Key.from_key_spec(val)


KeyRow = Sequence[Optional[Key]]
KeyBlock = Sequence[KeyRow]


class Layer(BaseModel):
    left: KeyBlock = Field(..., alias="keys")
    right: KeyBlock = []
    left_thumbs: KeyRow = []
    right_thumbs: KeyRow = []
    combos: Sequence[ComboSpec] = []

    class Config:
        allow_population_by_field_name = True

    @validator("left", "right", pre=True)
    def parse_key_block(cls, vals):
        return [cls.parse_key_row(row) for row in vals]

    @validator("left_thumbs", "right_thumbs", pre=True)
    def parse_key_row(cls, vals):
        return [Key.from_key_spec(val) for val in vals]


class Layout(BaseModel):
    split: bool = True
    rows: int
    columns: int
    thumbs: int = 0

    @root_validator
    def check_thumbs(cls, vals):
        if vals["thumbs"]:
            assert vals["thumbs"] <= vals["columns"], "Number of thumbs should not be greater than columns"
            assert vals["split"], "Cannot process non-split keyboard with thumb keys"
        return vals

    @property
    def total_keys(self):
        total = self.rows * self.columns
        if self.thumbs:
            total += self.thumbs
        if self.split:
            total *= 2
        return total

    @property
    def total_cols(self):
        return 2 * self.columns if self.split else self.columns

    def pos_to_col(self, pos: int):
        col = pos % self.total_cols
        if pos >= self.rows * self.total_cols and self.thumbs:
            col += self.columns - self.thumbs
        return col

    def pos_to_row(self, pos: int):
        return pos // self.total_cols


class KeymapData(BaseModel):
    layout: Layout
    layers: Mapping[str, Layer]
    combos: Sequence[ComboSpec] = []

    @root_validator(skip_on_failure=True)
    def assign_combos_to_layers(cls, vals):
        for combo in vals["combos"]:
            for layer in combo.layers if combo.layers else vals["layers"]:
                vals["layers"][layer].combos.append(combo)
        return vals

    @root_validator(skip_on_failure=True)
    def validate_split(cls, vals):
        if not vals["layout"].split:
            if any(layer.right or layer.left_thumbs or layer.right_thumbs for layer in vals["layers"].values()):
                raise ValueError("Cannot have right or thumb blocks for non-split layouts")
        return vals

    @root_validator(skip_on_failure=True)
    def check_combo_pos(cls, vals):
        for layer in vals["layers"].values():
            for combo in layer.combos:
                assert len(combo.positions) == 2, "Cannot have more than two positions for combo"
                assert all(pos < vals["layout"].total_keys for pos in combo.positions), \
                    "Combo positions exceed number of keys"
        return vals

    @root_validator(skip_on_failure=True)
    def check_dimensions(cls, vals):
        nrows, ncols, nthumbs = vals["layout"].rows, vals["layout"].columns, vals["layout"].thumbs
        for name, layer in vals["layers"].items():
            assert len(layer.left) == nrows and (not layer.right or len(layer.right) == nrows), \
                f"Number of rows do not match layout specification in layer {name}"
            for row in chain(layer.left, layer.right):
                assert len(row) == ncols, f"Number of columns do not match layout specification in layer {name}"
            assert len(layer.left_thumbs) == len(layer.right_thumbs) == nthumbs, \
                f"Number of thumb keys do not match layout specification in layer {name}"
        return vals


class Keymap:
    def __init__(self, **kwargs) -> None:
        kd = KeymapData(**kwargs)
        self.layout = kd.layout
        self.layers = kd.layers

        self.block_w = self.layout.columns * KEYSPACE_W
        self.block_h = (self.layout.rows + (1 if self.layout.thumbs else 0)) * KEYSPACE_H
        self.layer_w = (2 if self.layout.split else 1) * self.block_w + OUTER_PAD_W
        self.layer_h = self.block_h
        self.board_w = self.layer_w + 2 * OUTER_PAD_W
        self.board_h = len(self.layers) * self.layer_h + (len(self.layers) + 1) * OUTER_PAD_H

    @staticmethod
    def _draw_rect(x: float, y: float, w: float, h: float, cls: Optional[str] = None) -> None:
        class_str = f' class="{cls}"' if cls is not None else ""
        print(f'<rect rx="{KEY_RX}" ry="{KEY_RY}" x="{x}" y="{y}" width="{w}" height="{h}"{class_str}/>')

    @staticmethod
    def _draw_text(x: float, y: float, text: str, cls: Optional[str] = None) -> None:
        class_str = f' class="{cls}"' if cls is not None else ""
        words = text.split()
        if not words:
            return
        if len(words) == 1:
            print(f'<text x="{x}" y="{y}"{class_str}>{escape(words[0])}</text>')
            return
        print(f'<text x="{x}" y="{y}"{class_str}>')
        print(f'<tspan x="{x}" dy="-{(len(words) - 1) * 0.6}em">{escape(words[0])}</tspan>', end="")
        for word in words[1:]:
            print(f'<tspan x="{x}" dy="1.2em">{escape(word)}</tspan>')
        print('</text>')

    def print_key(self, x: float, y: float, key: Key, width: int = 1) -> None:
        key_width = (width * KEY_W) + 2 * (width - 1) * INNER_PAD_W
        self._draw_rect(x + INNER_PAD_W, y + INNER_PAD_H, key_width, KEY_H, key.type)
        self._draw_text(x + INNER_PAD_W + key_width / 2, y + KEYSPACE_H / 2, key.tap)
        self._draw_text(x + INNER_PAD_W + key_width / 2, y + KEYSPACE_H - LINE_SPACING / 2, key.hold, cls="small")

    def print_combo(self, x: float, y: float, combo_spec: ComboSpec) -> None:
        pos_idx = combo_spec.positions

        cols = [self.layout.pos_to_col(p) for p in pos_idx]
        rows = [self.layout.pos_to_row(p) for p in pos_idx]
        x_pos = [x + c * KEYSPACE_W + (OUTER_PAD_W if self.layout.split and c >= self.layout.columns else 0) for c in cols]
        y_pos = [y + r * KEYSPACE_H for r in rows]

        x_mid, y_mid = sum(x_pos) / len(pos_idx), sum(y_pos) / len(pos_idx)

        self._draw_rect(x_mid + INNER_PAD_W + KEY_W / 4, y_mid + INNER_PAD_H + KEY_H / 4, KEY_W / 2, KEY_H / 2, "combo")
        self._draw_text(x_mid + KEYSPACE_W / 2, y_mid + INNER_PAD_H + KEY_H / 2, combo_spec.key.tap, cls="small")

    def print_row(self, x: float, y: float, row: KeyRow) -> None:
        prev_key, width = None, 0
        for i, key in enumerate(chain(row, [None])):
            if i > 0 and (prev_key is None or key != prev_key or i == len(row)):
                self.print_key(x, y, prev_key or Key(tap=""), width=width)

                x += width * KEYSPACE_W
                width = 0

            prev_key = key
            width += 1

    def print_block(self, x: float, y: float, block: KeyBlock) -> None:
        for row in block:
            self.print_row(x, y, row)
            y += KEYSPACE_H

    def print_layer(self, x: float, y: float, name: str, layer: Layer) -> None:
        self._draw_text(KEY_W / 2, y - KEY_H / 2, f"{name}:", cls="label")
        self.print_block(x, y, layer.left)
        if layer.right:
            self.print_block(
                x + self.block_w + OUTER_PAD_W,
                y,
                layer.right,
            )
        if self.layout.thumbs and layer.left_thumbs and layer.right_thumbs:
            self.print_row(
                x + (self.layout.columns - self.layout.thumbs) * KEYSPACE_W,
                y + self.layout.rows * KEYSPACE_H,
                layer.left_thumbs,
            )
            self.print_row(
                x + self.block_w + OUTER_PAD_W, y + self.layout.rows * KEYSPACE_H, layer.right_thumbs
            )
        if layer.combos:
            for combo_spec in layer.combos:
                self.print_combo(x, y, combo_spec)

    def print_board(self) -> None:
        print(
            f'<svg width="{self.board_w}" height="{self.board_h}" viewBox="0 0 {self.board_w} {self.board_h}" '
            'xmlns="http://www.w3.org/2000/svg">'
        )
        print(f"<style>{STYLE}</style>")

        x, y = OUTER_PAD_W, 0
        for name, layer in self.layers.items():
            y += OUTER_PAD_H
            self.print_layer(x, y, name, layer)
            y += self.layer_h

        print("</svg>")


def main() -> None:
    with open(sys.argv[1], "rb") as f:
        data = yaml.safe_load(f)
    km = Keymap(**data)
    km.print_board()


if __name__ == "__main__":
    main()