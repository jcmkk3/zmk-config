/*
 * Copyright (c) 2020 Google LLC.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <init.h>
#include <drivers/pinmux.h>
#include <soc.h>

static int board_pinmux_init(const struct device *dev)
{
	const struct device *muxa = DEVICE_DT_GET(DT_NODELABEL(pinmux_a));
	const struct device *muxb = DEVICE_DT_GET(DT_NODELABEL(pinmux_b));

	ARG_UNUSED(dev);

	if (!device_is_ready(muxa)) {
		return -ENXIO;
	}
	if (!device_is_ready(muxb)) {
		return -ENXIO;
	}

#if ATMEL_SAM0_DT_SERCOM_CHECK(1, atmel_sam0_i2c) && defined(CONFIG_I2C_SAM0)
	/* SERCOM1 on SDA=PA16, SCL=PA17 */
	pinmux_pin_set(muxa, 16, PINMUX_FUNC_C);
	pinmux_pin_set(muxa, 17, PINMUX_FUNC_C);
#endif

#if ATMEL_SAM0_DT_SERCOM_CHECK(0, atmel_sam0_i2c) && defined(CONFIG_I2C_SAM0)
#warning Pin mapping may not be configured
#endif
#if ATMEL_SAM0_DT_SERCOM_CHECK(1, atmel_sam0_i2c) && defined(CONFIG_I2C_SAM0)
#warning Pin mapping may not be configured
#endif
#if ATMEL_SAM0_DT_SERCOM_CHECK(3, atmel_sam0_i2c) && defined(CONFIG_I2C_SAM0)
#warning Pin mapping may not be configured
#endif
#if ATMEL_SAM0_DT_SERCOM_CHECK(4, atmel_sam0_i2c) && defined(CONFIG_I2C_SAM0)
#warning Pin mapping may not be configured
#endif
#if ATMEL_SAM0_DT_SERCOM_CHECK(5, atmel_sam0_i2c) && defined(CONFIG_I2C_SAM0)
#warning Pin mapping may not be configured
#endif

#if ATMEL_SAM0_DT_SERCOM_CHECK(2, atmel_sam0_spi) && defined(CONFIG_SPI_SAM0)
	/* SPI SERCOM0 on MISO=PA09/pad 1, MOSI=PA10/pad 2, SCK=PA11/pad 3 */
	pinmux_pin_set(muxa, 9, PINMUX_FUNC_C);
	pinmux_pin_set(muxa, 10, PINMUX_FUNC_C);
	pinmux_pin_set(muxa, 11, PINMUX_FUNC_C);
#endif

#if ATMEL_SAM0_DT_SERCOM_CHECK(1, atmel_sam0_spi) && defined(CONFIG_SPI_SAM0)
#warning Pin mapping may not be configured
#endif
#if ATMEL_SAM0_DT_SERCOM_CHECK(2, atmel_sam0_spi) && defined(CONFIG_SPI_SAM0)
#warning Pin mapping may not be configured
#endif
#if ATMEL_SAM0_DT_SERCOM_CHECK(3, atmel_sam0_spi) && defined(CONFIG_SPI_SAM0)
#warning Pin mapping may not be configured
#endif
#if ATMEL_SAM0_DT_SERCOM_CHECK(4, atmel_sam0_spi) && defined(CONFIG_SPI_SAM0)
#warning Pin mapping may not be configured
#endif
#if ATMEL_SAM0_DT_SERCOM_CHECK(5, atmel_sam0_spi) && defined(CONFIG_SPI_SAM0)
#warning Pin mapping may not be configured
#endif

#if defined(CONFIG_USB_DC_SAM0)
	/* USB DP on PA25, USB DM on PA24 */
	pinmux_pin_set(muxa, 25, PINMUX_FUNC_G);
	pinmux_pin_set(muxa, 24, PINMUX_FUNC_G);
#endif

	return 0;
}

SYS_INIT(board_pinmux_init, PRE_KERNEL_2, CONFIG_PINMUX_INIT_PRIORITY);
