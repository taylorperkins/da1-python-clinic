"""FUNCTIONS LVL. 2

Functions can specify "parameters".
Parameters come in two flavors::
    * "Arguments" (required)
    * "Keyword arguments" (optional, has a default)


Parameters look like::

    # Arguments
    def my_func_with_args(arg1, arg2):
        print(f'{arg1} and {arg2} were required!')


    # Keyword Arguments
    def my_func_with_kwargs(kwarg1='foo', kwarg2='bar'):
        print(f'{kwarg1} and {kwarg2} were optional!')

"""

from typing import Any


def print_value(value: Any) -> None:
    """Prints anything!

    :param value:
    """
    print(value)


def multiply(number_1: int, number_2: int) -> int:
    """Multiplies the two!

    :param number_1: Left number
    :param number_2: Right number
    """
    return number_1 * number_2


def exponent(number: int, exp: int = 2) -> int:
    """Default is boxy (square..)

    :param number:
    :param exp: Specify an exponent, default is 2
    """
    return number**exp


if __name__ == '__main__':
    """A couple things are broken here.. What?"""

    print_value()

    print_value('Taylor!')

    print_value(multiply(4, 5))
    print_value(multiply(200, 300))
    multiply()

    print_value(exponent(2, 3))
    print_value(exponent(2))
