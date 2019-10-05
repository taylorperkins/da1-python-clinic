"""FUNCTIONS LVL. 5

The last level! For now..

Functions that return.. FUNCTIONS

We are talking about high-order functions, closures, and decorators.
"""
from time import sleep


def apply_func(func, a_list):
    """I am high order!"""
    return func(a_list)


def add_n(n=5):
    """I am a closure!!"""

    def inner(number):
        return number + n

    return inner


def log_time(func):
    """I am a decorator!"""

    from datetime import datetime

    def inner(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()

        print(f"Took {round((end - start).total_seconds(), 2)} seconds")
        return result

    return inner


def sleep_n_seconds(n=1):
    sleep(n)


@log_time
def sleep_n_seconds_v2(n=1):
    sleep(n)


if __name__ == '__main__':
    print(apply_func(sum, [1, 2, 3]))

    add_3 = add_n(3)
    print(add_3(4))
    print(add_3(10))

    def sleep_n_seconds(n=1):
        sleep(n)


    logged_sleep = log_time(sleep_n_seconds)
    logged_sleep(3)
