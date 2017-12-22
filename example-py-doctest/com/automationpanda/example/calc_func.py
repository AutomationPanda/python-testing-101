"""
This example has doctests in the module's docstrings.
Run tests with the "python -m doctest" command.
To generate an XML report, run this module directly to execute the main section.
"""


def add(a, b):
    """
    Adds two numbers.

    >>> add(3, 2)
    5

    :param a: first number
    :param b: second number
    :return: sum
    """

    return a + b


def subtract(a, b):
    """
    Subtracts two numbers.

    >>> subtract(3, 2)
    1
    >>> subtract(2, 3)
    -1

    :param a: first number
    :param b: second number
    :return: difference
    """

    return a - b


def multiply(a, b):
    """
    Multiplies two numbers.

    >>> multiply(3, 2)
    6

    :param a: first number
    :param b: second number
    :return: product
    """

    return a * b


def divide(a, b):
    """
    Divides two numbers.
    Automatically raises ZeroDivisionError.

    >>> divide(3.0, 2.0)
    1.5
    >>> divide(1.0, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: float division by zero

    :param a: first number
    :param b: second number
    :return: quotient
    """

    return a * 1.0 / b


def maximum(a, b):
    """
    Finds the maximum of two numbers.

    >>> maximum(3, 2)
    3
    >>> maximum(2, 3)
    3
    >>> maximum(3, 3)
    3

    :param a: first number
    :param b: second number
    :return: maximum
    """

    return a if a >= b else b


def minimum(a, b):
    """
    Finds the minimum of two numbers.

    >>> minimum(3, 2)
    2
    >>> minimum(2, 3)
    2
    >>> minimum(2, 2)
    2

    :param a: first number
    :param b: second number
    :return: minimum
    """

    return a if a <= b else b


if __name__ == "__main__":
    import doctest
    import xmlrunner

    suite = doctest.DocTestSuite()
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    runner.run(suite)
