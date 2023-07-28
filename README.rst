Introduction
============




.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/skerr92/Oakdevtech_CircuitPython_IcePython/workflows/Build%20CI/badge.svg
    :target: https://github.com/skerr92/Oakdevtech_CircuitPython_IcePython/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Usually to program an iCE40 FPGA from Lattice Semiconductor you need an FTDI chip or some other tool like OpenOCD and a device capable of communicating over SPI.
This has changed now with IcePython, a driver library for CircuitPython which allows you to program any iCE40 FPGA with a simple command.

Simply instantiate the IcePython class with a SPI object, a pin for chip select, and a pin for FPGA reset, and a filename, and you'r good to go. Calling `program_fpga()` then
programs the FPGA with the bin file provided. Be sure to include all the required dependencies. For usage details, please see the example in the examples directory.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!


On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/oakdevtech-circuitpython-icepython/>`_.
To install for current user:

.. code-block:: shell

    pip3 install oakdevtech-circuitpython-icepython

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install oakdevtech-circuitpython-icepython

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install oakdevtech-circuitpython-icepython

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install oakdevtech_icepython

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

examples folder and be included in docs/examples.rst.

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://circuitpython-icepython.readthedocs.io/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/skerr92/Oakdevtech_CircuitPython_IcePython/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
