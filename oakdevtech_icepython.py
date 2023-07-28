# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Seth Kerr for Oak Development Technologies
#
# SPDX-License-Identifier: MIT
"""
`oakdevtech_icepython`
================================================================================

A library for programming iCE40 FPGA from Lattice Semi


* Author(s): Seth Kerr

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s).
  Use unordered list & hyperlink rST inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies
  based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports
import time, digitalio, os, io
__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/skerr92/Oakdevtech_CircuitPython_IcePython.git"

class Oakdevtech_icepython:
  """Driver for programming Lattice Semiconductor iCE40 FPGA over SPI"""
  def __init__(self,spi,cs,reset,filename=None):
    self._spi = spi
    self._filename = filename
    self._reset = digitalio.DigitalInOut(reset)
    self._reset.direction = digitalio.Direction.OUTPUT
    self._chip_sel = digitalio.DigitalInOut(cs)
    self._chip_sel.direction = digitalio.Direction.OUTPUT
    self._reset.value = True
    self._chip_sel.value = True
    try:
      self._file = io.open(filename, mode='rb')
    except:
      if self._filename == None:
        print("\nNo filename provided")
      else:
        print("\nNo such file: ", self._filename)
    finally:
      print("\nfinished init...")


  def set_bin_file(self,filename):
    self._filename = filename

  def reset_fpga(self):
    self._reset.value = False
    time.sleep(0.1)
    self._reset.value = True

  def program_fpga(self):
    filecontents = self._file.read()
    if (len(filecontents) > 0):
      print("in the write of my life!")
      while not self._spi.try_lock():
        pass
      self._spi.configure(baudrate=1000000, phase=1, polarity=1)
      self._reset.value = False
      time.sleep(0.1)
      self._chip_sel.value = False
      self._reset.value = True
      time.sleep(0.1)
      self._chip_sel.value = True
      for i in range(0,7):
        self._spi.write(bytes(0))
      self._spi.write(filecontents)
      self._chip_sel.value = True
      for i in range(0,100):
        self._spi.write(bytes(0))
      self._chip_sel.value = False
      temp_buf = bytearray(2)
      self._spi.readinto(temp_buf)
      self._spi.unlock()
    else:
      print_err("No file contents")

