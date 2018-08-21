.. _index:

****************
docs-style-guide
****************

Documentation Style Guide for all projects under the Pylons Project


.. _installation:

Installation
============

.. code-block:: bash

    # Check out the project.
    git clone https://github.com/Pylons/docs-style-guide.git
    # Change your working directory to the project.
    cd docs-style-guide
    # Create a virtual environment.
    python3 -m venv env
    # Install the project in development mode.
    env/bin/pip install -e .


.. _building-documentation:

Building documentation
======================

We use tox to build the documentation and run tests.
Install tox into your user space or virtual environment.

From the project root, run tox.

.. code-block:: bash

    tox
