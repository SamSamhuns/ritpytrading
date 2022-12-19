ritpytrading
============

RIT-trading-python
------------------

|PyPI pyversions| |Build Status| |Updates| |PyPI version fury.io| |Python 3| |Codacy Badge| |License|

Disclaimer: The providers of the RIT software have refused to make the RestAPI public and I do not have access to the RIT server platform, therefore this repository might be out of date with the current version of RIT. It would be useful as a reference to create a more advanced automated trading API.

Python trading module for the Rotman Interactive Trader trading
software. `PyPI`_ page.

Install with pip: ``pip install ritpytrading``

Full documentation available `online.  <https://samsamhuns.github.io/docs/html/index.html>`_

A GitHub markdown flavor documentation can be found in ``documentation/README.md``.

.. image:: https://github.com/SamSamhuns/ritpytrading/blob/master/images/rit_image.PNG
    :width: 400px
    :align: left
    :height: 300px
    :alt: Image not available.

Requirements
------------

-   Python 3.6+

-   `The Rotman Interactive Trading Client <http://rit.rotman.utoronto.ca/software.asp>`_

The RIT Client only supports **Windows OS**. However, development of the PyPI ritpytrading package
can be in done in Linux/BSD environments as well.

The full documentation for the RIT Client REST API can be found at `Swaggerhub <https://app.swaggerhub.com/apis/306w/rit-client-api/1.0.0>`_.
The swagger API documentation is also provided in the ``swagger_client_generated`` folder.

Usage (Only on Windows)
---------------------------------------------

**IMPORTANT:**

* The RIT Trading Client must also be running to make sure the REST RIT API Client requests can be made.

* In each script your **RIT Client API key** must be entered and the **requests** module be imported to make API calls.

* The **API** and **API Orders** mode must be enabled in the RIT Client for the python module to send order requests.

::

   $ pip install ritpytrading

Examples scripts are present inside the ``examples`` folder. Documentation available `here.  <https://samsamhuns.github.io/docs/html/index.html>`_

Developers Guide
________________

Setup
~~~~~

RIT Client
~~~~~~~~~~

The RIT Client for Windows can be downloaded at
http://rit.rotman.utoronto.ca/software.asp.

Instructions for setting up an RIT demonstration client account for the
Liability Trading 3 case file can be found at
http://rit.rotman.utoronto.ca/demo.asp.


Windows
~~~~~~~

Initialize the repository with git.
Detailed instructions to download git for windows can be found at `atlassian <https://www.atlassian.com/git/tutorials/install-git#windows>`_.  The repository can then be initialized with git using:

::

   $ git clone https://github.com/SamSamhuns/RIT-trading-python

Two options are available after this:

-  Anaconda is recommended for Windows system. Set up up a virtual conda environment first.
   Then open the anaconda prompt and use the command ``conda install --yes --file requirements.txt``
   to install all modules from requirements.txt.

-  Or Install \ ``python``\  and add it to your ``PATH`` system variable.
   Then install the \ ``pip``\  package if not installed already also adding it to the ``PATH`` system variable.
   Then run the following commands.

::

   $ python -m venv venv
   $ .\venv\Scripts\activate
   $ pip install -r requirements.txt

Note: When using **PowerShell** in Windows, the virtual environment has to be activated with ``.\venv\Scripts\activate.ps1``

Linux/BSD
~~~~~~~~~

After cloning the repository, install packages using pip.

::

   $ git clone https://github.com/SamSamhuns/RIT-trading-python
   $ python -m venv venv
   $ source venv/bin/activate
   $ pip install -r requirements.txt

Building dists and running tests using makefile
-----------------------------------------------

For **Windows**, different options are available for using makefile. `GnuWin's make`_
provides a native port for Windows (without requiring a full runtime environment like Cygwin).
After installing GnuWin, add ``C:\Program Files (x86)\GnuWin32\bin``
to your system ``PATH`` variable to run makefiles from any directory.

-  For **Windows**, run makefile commands with ``make -f Makefile.win <directive>``. Example ``make -f Makefile.win help``
-  For **Linux/BSD**, run makefile commands with ``make <directive>``.

Run the following command to get a list of all Makefile command options.

::

  $ make help

To run tests.

::

  $ make test
  $ make test-all

To ensure the README.rst will be rendered in PyPi [If deprecated use the twine command given below]

::

  $ python setup.py check --restructuredtext

To ensure the README.rst renders properly. After building with ``make dist``, check the rendering with:

::

  $ twine check dist/*

To build the source and wheel package.
::

  $ make dist

To upload the distribution code to PyPi. The version number must be updated in ``setup.py`` and logged in ``HISTORY.rst``.
::

  $ twine upload dist/*

Running tests with the python unittest module
---------------------------------------------

Once python has been added to the ``PATH`` system variable in Windows,
the code for running the scripts on Windows and Linux/BSD based systems
are the same.

From the main directory, run:

::

   $ python -m unittest

If no tests are run from the command above, run the verbose mode.

Verbose mode

::

   $ python -m unittest discover -v

Authors
-------

-  **Samridha Shrestha**

License
-------

This project is licensed under the Apahce 2.0 License - see the
`LICENSE.md <LICENSE.md>`__ file for details

Acknowledgments
---------------

-  Rotman School of Manangement, University of Toronto
   http://www.rotman.utoronto.ca/
-  Rotman Interactive Trader http://rit.rotman.utoronto.ca/
-  Python open source libraries
-  Joel Hasbrouck, NYU Stern Principles of Securities Trading,
   FINC-UB.0049, Spring 201. http://people.stern.nyu.edu/jhasbrou/
-  This project directory was created based on Cookiecutter_ and
   the `audreyr/cookiecutter-pypackage`_ project template.
-  README conversion for PyPI. `Pandoc.org`_.

Contributions
-------------

|contributions welcome|

Disclaimer
----------

All RIT software and external RIT links are provided by the Rotman
School of Management and are their exclusive property.

.. |Build Status| image:: https://app.travis-ci.com/SamSamhuns/ritpytrading.svg?branch=master
    :target: https://app.travis-ci.com/SamSamhuns/ritpytrading
.. |Updates| image:: https://pyup.io/repos/github/SamSamhuns/ritpytrading/shield.svg
   :target: https://pyup.io/repos/github/SamSamhuns/ritpytrading/
.. |Python 3| image:: https://pyup.io/repos/github/SamSamhuns/ritpytrading/python-3-shield.svg
   :target: https://pyup.io/repos/github/SamSamhuns/ritpytrading/
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/6a873df3e02c4950add070885d3a4e8b
   :alt: Codacy Badge
   :target: https://app.codacy.com/gh/SamSamhuns/ritpytrading?utm_source=github.com&utm_medium=referral&utm_content=SamSamhuns/ritpytrading&utm_campaign=Badge_Grade_Settings
.. |License| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0
.. |contributions welcome| image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
   :target: https://github.com/SamSamhuns/ritpytrading/pulls
.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/ritpytrading.svg
   :target: https://pypi.python.org/pypi/ritpytrading/
.. |PyPI version fury.io| image:: https://badge.fury.io/py/ritpytrading.svg
   :target: https://pypi.python.org/pypi/ritpytrading/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`Pandoc.org`: https://pandoc.org/
.. _`PyPI`: https://pypi.org/project/ritpytrading/
.. _`GnuWin's make`:  http://gnuwin32.sourceforge.net/packages/make.htm
