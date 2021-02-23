================================================
Welcome to Rational Activations's documentation!
================================================

.. highlight:: python

Rational Activations provided in this package are learnable rational activation
function to create rational neural networks.
So far, only the pytorch and MXNET implementation are available.

Requirements:
#############
This project depends on:

- pytorch
- numpy, scipy (if you want to add different initially approximated functions)
- matplotlib (if you want to use the plotting properties)

Download and install:
You can download from the
`Github <https://github.com/ml-research/activation_functions>`_ repository or:

::

    pip3 install rational-activations

To use it:

.. literalinclude:: tutorials/code/how_to_use_rationals.py
   :lines: 1-6

.. toctree::
    :maxdepth: 2
    :caption: Tutorials:
    :glob:

    tutorials/*


.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: API:
   :glob:

   rational_modules/*

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
