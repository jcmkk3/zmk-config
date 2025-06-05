# Layout
## Overview
```
alphas:                                       edit:                                    
 x   c   l   f   p    k   y   o   u   '       all udo esc del f2   pg↑ hme  ↑  end top 
 r   s   d   f   b    j   h   e   l   a       gui sft ctl alt f5   pg↓  ←  ent  →  btm 
     x   m   g            d   ,   .               cut cpy pst          bsp  ↓  tab     
            edt spc  upp sym                              edt spc  upp sym             
                                                          ^^^                          
numbers:                                      symbols:                                 
 !   @   #   $   %    ^   &   ;   :   ?        !   @   #   $   %    ^   &   ;   :   ?  
 1   2   3   4   5    6   7   8   9   0        ~   =   +   *   `    \  alt ctl sft gui 
     _   -   /            |   ,   .                _   -   /            |   <   >      
            edt spc  upp sym                              edt spc  upp sym             
            ^^^          ^^^                                           ^^^             
combos:                                                                                
~vv~~ ~~~~~    ~~qq~ ~~~~~    ~~~~~ ~~~~~     ~[~~~ ~~~]~    ~~{~~ ~~}~~    ~~~(~ ~)~~~
~~~~~ ~~~~~    ~~~~~ ~~~~~    ~~~~~ ~~~~~     ~[~~~ ~~~]~    ~~{~~ ~~}~~    ~~~(~ ~)~~~
 ~~~   ~~~      ~~~   ~~~      xx~   ~~~       ~~~   ~~~      ~~~   ~~~      ~~~   ~~~ 
```
The primary goal is to stay in the flow while using the keyboard, for the ways that "I" use a keyboard. Those ways include writing prose, writing code and interacting with my computer (e.g. application shortcuts and shell commands).

### The physics of staying in the flow

| Finger | Range of motion             | Speed  | Hold Strength |
|--------|-----------------------------|--------|---------------|
| Pinky  | Low                         | Low    | Low           |
| Ring   | Medium                      | Low    | High          |
| Middle | High                        | Medium | High          |
| Index  | Medium (vertical & lateral) | High   | Medium        |
| Thumb  | Medium (lateral)            | Low    | High          |

#### Good vs bad key positions
Which keys are nicest to press for me, likely won't be the same for others. It is a combination of keyboard, [hand/body positioning](#Hand position and its affects on layout), and personal biology (e.g. finger range of motion)

#### Hold vs press vs multi-press vs ...
Fingers with higher speed are best for keys that need to be quickly repeated (e.g. delete, arrows). Fingers with higher hold strength are better for keys that need to be held (e.g. ctrl, shift, layers).

#### Sequences with same finger
Even if a key might be on a good finger in isolation, it might be a bad fit in common sequences with other keys. It is best to avoid SFBs (same finger bigrams). In cases where this can't be avoided, it is ideal to position the bigram as a slide down with the finger. It is also best handled by a finger with higher speed.

#### Sequences with same hand
Sequences that happen on the same hand can feel good if the keys flow together. There are many combinations that are best to avoid, however. Redirects are when the sequence of keys changes directions on the same hand. LSBs (lateral stretch bigrams) are cases like a sequence that goes from the middle column to the inner column. Scissors are particular sequences of keys on adjacent fingers which skip between bottom/top rows.

#### Spread load across all fingers
It could be easy to optimize for some of the above points and then realize that one or two fingers are carrying a disproportionate amount of the load. Not all fingers are equal, however, so the expectation is not that each finger will have 10% of the load. I don't have particular numbers, but I try to keep the overall balance in mind.


### Design Guidelines
There are many ways to optimize for some of the physical constraints above. The challenge is doing it in a way that keeps the cognitive complexity managable.

#### Avoid fancy features
Focus on grouping and positioning keys for optimal use/re-use in different situations. Be deliberate about where each key is placed. What keys does it combine with? What functions does it serve throughout different applications? How to rember where it is placed?

#### Avoid stateful behavior if possible
e.g. capslock, numlock, toggle layers, sticky keys

#### Avoid timing based behavior if possible
e.g. mod-tap, layer-tap

#### Avoid special cased functionality
e.g. application specific shortcuts, same key in multiple places
Ideally, a key will be placed where it can be used in all contexts that it would be used on a standard keyboard layout. In cases where a key would be needed on multiple layers, it is best if it is in the same spot on each layer

#### Favor simple features that put more functionality within reach
e.g. layers
Layers are conceptually simple. They work well when common sequences of keys are on same layer. Amortizes the cost of the extra key to activate layer. Any time you'd need to use a modifier to access that key on a normal layout, the cost is free, but there's potential to use more keys on that layer. 

#### Use common knowledge to your advantage
Consider where the key exists on a normal layout (both in relation to left/right side, row, and relative to other keys). If it is possible to position it in the same (or similar) position and there is not a major downside, then best to keep it there. Never know what software is going to try to take advantage of those positional attributes. It tends to be less friction this way.

#### Make it easy to remember
In cases where there are multiple equally good positions for a key, I try to position them in some way with a mnemonic significance.

#### Sprinkle in more advanced features sparringly
e.g. combos, mod morphs
Sometimes using a more advanced feature can open up the layout to strategies that wouldn't be possible otherwise. For instance, placing brackets (`)`, `}`, `]`) on combos allowed all other symbols to fit on the alphas or symbols layers. See the [combos](#Combos) section for more details. See how mod morphs are used in the [Edit](#Edit) section.

## Alphas
```
 x   c   l   f   p    k   y   o   u   '  
 r   s   d   f   b    j   h   e   l   a  
     x   m   g            d   ,   .      
            edt spc  upp sym             
```
### Bird

Bird was designed holistically to fit within the rest of my layout. See [bird](github) for more information about the bird layout.

How many letters actually change hands? Keyboard shortcuts can take hand into account if the expectation is that the shortcuts would be used along with a mouse (in the right hand).

Single quote for minimum SFB

, and . in standard places. More SFBs, but not the same as an SFB within a word. They form a natural pause. Stats are less important than muscle memory (mneumoncs) and LSB or higher pinky usage.

The alpha layout affects much more than just prose. They also play an integral role in application control as keyboard shortcuts (see editor section in addendum).

### Thumb keys

Dedicated layer keys

Edit, Space, Upper, Symbols. Why?

Use with mouse: shortcuts on Edit layer useful for one-handed use. Space used with mouse in creative applications (panning: verify).

Avoid SFB: Symbols are commonly followed by space. Shift+i (I) common bigram. Writing in all caps.

The other forms of whitespace are on the Edit layer (enter, tab). They are rarely used in sequence with space. They also are prone to the same bigrams from above so keeping them with space helps avoid SFBs.

Edit and Symbols pressed together activate Numbers. Having these in mirrored positions makes this most intuitive.

Shift is not sticky. Why?

## Combos
```
~vv~~ ~~~~~    ~~qq~ ~~~~~    ~~~~~ ~~~~~
~~~~~ ~~~~~    ~~~~~ ~~~~~    ~~~~~ ~~~~~
 ~~~   ~~~      ~~~   ~~~      xx~   ~~~ 
                                         
~[~~~ ~~~]~    ~~{~~ ~~}~~    ~~~(~ ~)~~~
~[~~~ ~~~]~    ~~{~~ ~~}~~    ~~~(~ ~)~~~
 ~~~   ~~~      ~~~   ~~~      ~~~   ~~~ 
```

Bigrams with almost everything

Often the closing bracket is autocompleted so really only one combo activation needed

Frees up space on symbol layer

Also good if using keybindings like vim unimpared

Round brackets (parenthesis)

On index because . (and maybe ,) can commonly follow

It is the only bracket commonly used in prose. Don't want it on the same finger as "e" since "e" is the most common ending letter

Curly brackets

Used for blocks/scope and object literals

Square brackets

Used for list/array literals and indexing

## Edit
```
all udo esc del f2   pg↑ hme  ↑  end top 
gui sft ctl alt f5   pg↓  ←  ent  →  btm 
    cut cpy pst          bsp  ↓  tab     
            edt spc  upp sym             
            ^^^                          
```
Left side focuses on keys/shortcuts that are useful when used with mouse in right hand. Right hand keys are the primary keyboard navigation and some editing commands.

Cut/copy/paste/undo/select all. Exception to "avoid special case rule".

Shift+copy and Shift+paste are easy to press. These are used for copy/paste from the system clipboard in terminal emulators since terminal applications often use the standard copy/paste shortcuts for different uses. Those shortcuts were part of the CUA standard that was established primarily for GUI applications, after terminal shortcut standards were already established. Shift+paste is also "paste as text" in many applications (even outside of Office?) and is easy to press.

FAQ: Need to go to a layer to access backspace, enter, tab, etc? Yes. It sounds weird at first, but there are many advantages once you get used to it. Call back to performing sequences of keys on the same layer and there are lots of examples of how that plays out on the edit layer.

Supress ctrl on home/end, add dedicated top/bottom

Bonus: ctrl+enter and shift+enter is often used to execute code, ctrl+shift+e is also commonly used to execute code (is it really?). enter and e are in the same position on different layers (mnemonic)

Shift+backspace mod-morphs to do delete. This makes it consistent-ish with how Tab/Shift+Tab work in most applications. Conceptually, I think of the left delete as "delete selected item". This is usually an item selected by the mouse (e.g. file/folder in file manager, shape/line in drawing program, etc). I think of the right backspace and shift+backspace as "delete character before/after cursor". Using ctrl+{shift}+backspace will do the same before/after only a "word" at a time.

Bonus: ctrl+alt+del = ctrl+shift+alt+backspace (home row ring+middle+index on left hand and lower index on right hand)

I often use Rename (F2) after selecting an item with my mouse. (how ubiquitous is F2 for rename?)

Tab

Use it to trigger autocomplete, but tend to less often spam it for autocomplete because up/down arrows are so close so I'm more likely to reach for them, then hit enter/space to complete

With the exception of GUI, the pinky keys perform functionality that only makes sense to press a single time. Pressing again won't do anything more.

Bonus: Some common keyboard shortcuts in spreadsheet applications
* "Top" goes to the first cell in the sheet
* "Bottom" goes to last cell (bottom-right) in range
* "Rename" to edit cell
* Check others

## Symbols
```
 !   @   #   $   %    ^   &   ;   :   ?  
 ~   =   +   *   `    \  alt ctl sft gui 
     _   -   /            |   <   >      
            edt spc  upp sym             
                         ^^^             
```
Why not combos? SFBs (including repeats)

Symbol layer and number layer considered together because the number layer is layered on top of the symbol layer

This reduces the amount of keys to remember per layer since many will be the same between layers

Visual: Num layer shown with symbol key positions blank and highlighted

Symbol keys on num row are prioritized for number based "words" and not for mathmetical formulas/calculation

Modifiers on homerow of hand that activates the layer w/ visual

Top row follows order of standard shifted numrow (up until `*`) w/ visual

Basic arithmetic operators w/ visual

Grouped in a block on best (available) positions opposite the activating hand/mods

`-` and `/` on bottom since they are most significant to number based "words"

Negative numbers: `-25`

Dates: `2025-04-28` or `4/28/2025`

`=` participates in many bigrams so their position in relation to common bigrams is important to avoid same finger bigramsis not on the same finger as any of the common operators used for compound assignment (`!=`, `+=`, `-=`, `*=`, `%=`, `/=`, `&=`, `|=`, `:=`, `^=`, `~=`, `<=`, `>=`, `=>`, `<=`, `==`) SFB: `@=`, which is a valid compound assignment operator in python but is very uncommon

`*` and `/` on fastest finger because they have common repeats

Markdown bold `**`

Org-mode headers `**{n}`

C-style language line comments `//`, and doc comments `///`, `////`

`++` and `--` pre/post increment/decrement (on slower finger, but still not bad. Not pinky)

Bonus: `+/-` symbols in logical vertical orientation for `ctrl-{+/-}` zooming

mod-morphed. With `ctrl`, it actually outputs `ctrl+=`, since that is commonly used for zooming in. Some application don't care if you use `=` or `+` for zooming in, but others only except `=` so this smooths out that paper cut. For "bigger" zoom that is `ctrl+shift+plus`, it already works as expected since `=` shifted is `+`.

Symbols that are unshifted on standard layout on opposite hand from mods w/ visual

These are most likely to be used for shortcuts with mods. Shortcuts using shifted symbols are akward.

`\`` on fastest finger because it has common repeats

Markdown/djot code fences/blocks `\`\`\``

`<` and `>` In same position as its shifted state on base layer (mnemonic).

Not on combos like other paired symbols `({[`. They are much more likely to be used in ways that aren't surrounding text like the other paired symbols.

They participate in many bigrams so their position in relation to common bigrams is important to avoid same finger bigrams (`<`, `>`, `<=`, `>=`, `=>`, `<=`, `->`, `<-`, `<!`, `~>`, `|>`, `<|`, `<>`, `%>%`, `<:`) SFB: `:>` (maybe? I think that I've seen it somewhere)

`;` and `:` on same fingers as `,` and `.` (mnemonic)

`|`

Positioned to make the common pipe bigrams `<|`, `|>` as comfortable as possible

On same finger as & which is often used opposite of `|` for bit manipulation or shortcuting and/or

`\``

Bonus: Most of the common bit/logical operators all together on right hand

`~` is in similar position (far left and next to `!`) to US QWERTY layout.

`~` and `!` on same finger. Both "not"-ish.

`~/` is a nice inward roll

`\`` and `~` are in same hand mirrored position

Back tick and back slash mirror each other

It would be aesthetically and mneumonically nice for forward slash and back slash to be mirrored, but there are no good positions to do that without sacrificing more than was gained. Besides, the two slash types don't actually have much, if anything, to do with each other except for how they look. They aren't used in pairs. They aren't opposites of each other in any use case that I know. Forward slash is much more important and used than back slash.

Note: Backslash is an exception to the rule for non-shifted symbols to go on the opposite hand from the mods. In practice, I haven't found any cases where it is used modified. If it was needed, its position actually allows it to be modified anyway.

`?` mirrors `!`

`??` is a repeat. Pinky is the worst finger for it, but it is a compromise.

Double quote is on alpha layer only because an opening quote is usually followed immediately by a letter and it is not uncommon for the letter to be uppercase so it is a better flow to have it on shift.


## Numbers
```
 !   @   #   $   %    ^   &   ;   :   ?  
 1   2   3   4   5    6   7   8   9   0  
     _   -   /            |   ,   .      
            edt spc  upp sym             
            ^^^          ^^^             
```
Numbers on home row in same order as standard number row

Number row has least amount of SFB

Isn't 1 and 0 being on pinky bad (they are some of the most common numbers)?

It isn't ideal, but they are on home-row pinky which is not bad.

In practice, it has not been a pain point

Having standard numrow ordering has been a better tradeoff (for mneumonics and positional shortcuts)

, and . replace < and > on number layer

All other symbol positions (outside of number row) are same as symbol layer

FAQ: Why symbols gets priority over numbers?

Programmers dvorak/workman

Conditional layers with dedicated layer keys

Can bounce between layers with no hesitation

## Addendum
### Hand position and its affects on layout
### What to do about modifiers
Why not mod-taps?

Note: the approach that I take is not at odds with mod-taps. It would be easy to layer on mod-taps and the approach would be similar to that of miryoku (exception is thumb shift and not HRM shift.

Mods started as callum mods, but now have no stickiness. Why?

Order of mods

Based on frequency and finger hold strength
### Editors
#### Vim
#### Emacs
