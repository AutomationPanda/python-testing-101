Python Testing Example: unittest
================================
This is the example project for
[Python Testing 101: doctest](https://automationpanda.com/2017/03/06/python-testing-101-doctest/),
part of the
[Python Testing 101 series](https://automationpanda.com/2017/03/06/python-testing-101-introduction/)
from [Automation Panda](https://automationpanda.com/).
It will work for Python 2 and 3.

Project Structure
-----------------
This project has two packages:
* `com.automationpanda.example` contains `calc.py`, which has a basic Calculator class.
* `com.automationpanda.tests` contains `test_calc.py`, which contains `unittest` test cases.

Running Tests
-------------

To run tests from the example project root directory, run one of the following commands:

* `python -m unittest discover` to discover all unit tests in a project
* `python -m unittest com.automationpanda.tests.test_calc` to run the test module by name
* `python -m unittest com.automationpanda.tests.test_calc.CalculatorTest` to run a TestCase class by name
* `python -m unittest com/automationpanda/tests/test_calc.py` to run the test module by file path

Note that unittest tests must be in a Python package from the project root,
meaning that the `tests` directory needs `__init__.py`.

To generate XML test reports, install `unittest-xml-reporting` and run:

* `python -m com.automationpanda.tests.test_calc`

XML reports will be printed to the `test-reports` directory.
