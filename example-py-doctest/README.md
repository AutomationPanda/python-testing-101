Python Testing Example: doctest
===============================
This is the example project for
[Python Testing 101: doctest](https://automationpanda.com/2017/03/06/python-testing-101-doctest/),
part of the
[Python Testing 101 series](https://automationpanda.com/2017/03/06/python-testing-101-introduction/)
from [Automation Panda](https://automationpanda.com/).
It will work for Python 2 and 3.

Project Structure
-----------------
This project has two modules:
* `com.automationpanda.example.calc_func` contains math functions.
  Doctests are embedded in function docstrings.
* `com.automationpanda.example.calc_class` contains a basic Calculator class.
  Doctests appear in a separate text file at `doctests/test_calc_class.txt`.

Running Tests
-------------
For `com.automationpanda.example.calc_func`:
* `python -m doctest com/automationpanda/example/calc_func.py` to run the tests.
* `python com/automationpanda/example/calc_func.py` to run the tests and generate XML reports.

For `com.automationpanda.example.calc_class`:
* `python -m doctest doctests/test_calc_class.txt` to run the tests in the separate text file.

*Warning*: By default, doctests will not print anything if tests are successful.
Add the `-v` option to print verbose output.