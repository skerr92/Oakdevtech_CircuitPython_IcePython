# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Seth Kerr for Oak Development Technologies
#
# SPDX-License-Identifier: Unlicense

"""
Example showing how to program an iCE40 FPGA with circuitpython!
"""

import time
import board
import oakdevtech_icepython

iceprog = oakdevtech_icepython.Oakdevtech_icepython(
    board.SPI(), board.A5, board.A4, "top.bin"
)

timestamp = time.monotonic()

iceprog.program_fpga()

endstamp = time.monotonic()
print("done in: ", (endstamp - timestamp), "seconds")

print("done")
