"""Timedelta!!
represents a duration, the difference between two dates or times.
https://docs.python.org/2/library/datetime.html#timedelta-objects

Signature::

    date_stuff.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
        * Note that all arguments are "optional", and default to 0


Main attributes::

    .days::
        timedelta in days

    .seconds::
        timedelta in seconds

    .microseconds::
        timedelta in microseconds


Main methods::

    .total_seconds()::
        Return the total number of seconds contained in the duration.


Fun Operations::

    | V1        | Op       | V2        | Returns
    __________________________________________
    | timedelta | -        | timedelta | timedelta
    | timedelta | +        | timedelta | timedelta
    | timedelta | *        | int       | timedelta
    | timedelta | //       | int       | timedelta
"""

from datetime import timedelta


if __name__ == '__main__':

    my_delta = timedelta()
    print(my_delta, type(my_delta))
    print(my_delta.days, my_delta.seconds, my_delta.microseconds)

    print(my_delta - timedelta(hours=5))
    print((my_delta + timedelta(days=5)) * 4)

    assert ((my_delta + timedelta(days=5)) * 4) == timedelta(days=20)

