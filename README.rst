lib_detect_testenv
==================


Version v2.0.3 as of 2023-01-13 see `Changelog`_

|build_badge| |license| |jupyter| |pypi| |pypi-downloads| |black|

|codecov| |cc_maintain| |cc_issues| |cc_coverage| |snyk|



.. |build_badge| image:: https://github.com/bitranox/lib_detect_testenv/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/bitranox/lib_detect_testenv/actions/workflows/python-package.yml


.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/bitranox/lib_detect_testenv/master?filepath=lib_detect_testenv.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/lib-detect-testenv?label=PyPI%20Package
   :target: https://badge.fury.io/py/lib_detect_testenv

.. |codecov| image:: https://img.shields.io/codecov/c/github/bitranox/lib_detect_testenv
   :target: https://codecov.io/gh/bitranox/lib_detect_testenv

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/lib_detect_testenv?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/lib_detect_testenv/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/lib_detect_testenv?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/lib_detect_testenv/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/lib_detect_testenv?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/lib_detect_testenv/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://img.shields.io/snyk/vulnerabilities/github/bitranox/lib_detect_testenv
   :target: https://snyk.io/test/github/bitranox/lib_detect_testenv

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/lib-detect-testenv
   :target: https://pypi.org/project/lib-detect-testenv/
   :alt: PyPI - Downloads

detects test environments: pytest, doctest and pycharm docrunner

----

automated tests, Travis Matrix, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.6.0 or newer

tested on recent linux with python 3.7, 3.8, 3.9, 3.10, 3.11, pypy-3.8 - architectures: amd64

`100% code coverage <https://codecov.io/gh/bitranox/lib_detect_testenv>`_, flake8 style checking ,mypy static type checking ,tested under `Linux, macOS, Windows <https://github.com/bitranox/lib_detect_testenv/actions/workflows/python-package.yml>`_, automatic daily builds and monitoring

----

- `Try it Online`_
- `Usage`_
- `Usage from Commandline`_
- `Installation and Upgrade`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/lib_detect_testenv/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/lib_detect_testenv/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/lib_detect_testenv/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----

Try it Online
-------------

You might try it right away in Jupyter Notebook by using the "launch binder" badge, or click `here <https://mybinder.org/v2/gh/{{rst_include.
repository_slug}}/master?filepath=lib_detect_testenv.ipynb>`_

Usage
-----------

- detect if test environment is active

.. code-block:: python

    def is_testenv_active(arg_string: Optional[str] = None) -> bool:
        """
        returns True if test environment is detected ("pytest", "doctest", "setup.py test")


        Parameter
        ----------
        arg_string  : optional, if None : str(sys.argv())


        Result
        ----------
        True if Test environment is detected


        Exceptions
        ----------
        none


        Examples
        ----------

        >>> assert is_testenv_active() == True
        """

- detect if doctest is active

.. code-block:: python

    def is_doctest_active(arg_string: Optional[str] = None) -> bool:
        """
        returns True if pycharm "docrunner.py" or "doctest.py" is detected


        Parameter
        ----------
        arg_string  : optional, if None : str(sys.argv())


        Result
        ----------
        True if docrunner is detected


        Exceptions
        ----------
        none

        """

- detect if pytest is active

.. code-block:: python

    def is_pytest_active(arg_string: Optional[str] = None) -> bool:
        """
        returns True if "pytest" is detected


        Parameter
        ----------
        arg_string  : optional, if None : str(sys.argv())


        Result
        ----------
        True if pytest is detected


        Exceptions
        ----------
        none

        """

- detect if setup.py is active

.. code-block:: python

    def is_setup_active(arg_string: Optional[str] = None) -> bool:
        """
        returns True if "setup.py" is detected


        Parameter
        ----------
        arg_string  : optional, if None : str(sys.argv())


        Result
        ----------
        True if setup.py is detected


        Exceptions
        ----------
        none

        """

- detect if "setup.py test" is active

.. code-block:: python

    def is_setup_test_active(arg_string: Optional[str] = None) -> bool:
        """
        returns True if "setup.py test" is detected


        Parameter
        ----------
        arg_string  : optional, if None : str(sys.argv())


        Result
        ----------
        True if "setup.py test" is detected


        Exceptions
        ----------
        none

        """

- add a path to the syspath

.. code-block:: python

    def add_path_to_syspath(path_to_append: PathLikeOrString) -> None:
        """
        adds a path to the syspath

        Parameter
        ----------
        path_to_append
            the path to append - will be resolved by this function and added to syspath
            if path_to_append is a file, its parent directory will be added.


        Result
        ----------
        none


        Exceptions
        ----------
        none


        Examples
        ----------

        >>> add_path_to_syspath(pathlib.Path(__file__).parent)
        >>> path1 = str(sys.path)
        >>> add_path_to_syspath(pathlib.Path(__file__))
        >>> path2 = str(sys.path)
        >>> assert path1 == path2
        """

- put this in Your `__init__.py` to automatically add the package directory to the syspath if the test environment is active.
  This is useful for local testing of packages.

.. code-block:: python

    # __init__.py :
    # this should be Your first import in __init__
    from lib_detect_testenv import *
    if is_testenv_active():
        add_path_to_syspath(__file__)

Usage from Commandline
------------------------

.. code-block::

   Usage: lib_detect_testenv [OPTIONS] COMMAND [ARGS]...

     detects if pytest or doctest or pyrunner on pycharm is running

   Options:
     --version                     Show the version and exit.
     --traceback / --no-traceback  return traceback information on cli
     -h, --help                    Show this message and exit.

   Commands:
     info  get program informations

Installation and Upgrade
------------------------

- Before You start, its highly recommended to update pip and setup tools:


.. code-block::

    python -m pip --upgrade pip
    python -m pip --upgrade setuptools

- to install the latest release from PyPi via pip (recommended):

.. code-block::

    python -m pip install --upgrade lib_detect_testenv

- to install the latest version from github via pip:


.. code-block::

    python -m pip install --upgrade git+https://github.com/bitranox/lib_detect_testenv.git


- include it into Your requirements.txt:

.. code-block::

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    lib_detect_testenv

    # for the latest development version :
    lib_detect_testenv @ git+https://github.com/bitranox/lib_detect_testenv.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt


- to install the latest development version from source code:

.. code-block::

    # cd ~
    $ git clone https://github.com/bitranox/lib_detect_testenv.git
    $ cd lib_detect_testenv
    python setup.py install

- via makefile:
  makefiles are a very convenient way to install. Here we can do much more,
  like installing virtual environments, clean caches and so on.

.. code-block:: shell

    # from Your shell's homedirectory:
    $ git clone https://github.com/bitranox/lib_detect_testenv.git
    $ cd lib_detect_testenv

    # to run the tests:
    $ make test

    # to install the package
    $ make install

    # to clean the package
    $ make clean

    # uninstall the package
    $ make uninstall

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    click
    cli_exit_tools

Acknowledgements
----------------

- special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"

Contribute
----------

I would love for you to fork and send me pull request for this project.
- `please Contribute <https://github.com/bitranox/lib_detect_testenv/blob/master/CONTRIBUTING.md>`_

License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

---

Changelog
=========

- new MAJOR version for incompatible API changes,
- new MINOR version for added functionality in a backwards compatible manner
- new PATCH version for backwards compatible bug fixes

v2.0.3
---------
2023-01-13:
    - update github actions : checkout@v3 and setup-python@v4
    - remove "better code" badges
    - remove python 3.6 tests
    - add python 3.11 tests
    - update to pypy 3.9 tests

v2.0.2.2
---------
2022-06-02: update to github actions checkout@v3 and setup-python@v3

v2.0.2.1
--------
2022-06-01: update github actions test matrix

v2.0.2
--------
2022-03-29: remedy mypy Untyped decorator makes function "cli_info" untyped

v2.0.1
--------
2022-03-25: fix github actions windows test

v2.0.0
-------
2021-11-23:
    - add "setup.py test" detection

v1.0.2
-------
2021-11-22:
    - remove second github action yml
    - fix "setup.py test"

v1.0.1
------
2021-11-21: implement github actions

v1.0.0
------
2021-11-19: initial release

