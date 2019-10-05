"""Time!!
represents a (local) time of day, independent of any particular day
https://docs.python.org/2/library/datetime.html#time-objects

Signature::

    date_stuff.time([hour[, minute[, second[, microsecond[, tzinfo]]]]])
        * Note that all arguments are optional


Main attributes::

    .hour::
        hour as a number

    .minute::
        minute as a number

    .second::
        second as a number

    .microsecond::
        microsecond as a number


Main methods::

    .replace([hour[, minute[, second[, microsecond[, tzinfo]]]]])::
        Replace one of the values you specify

    .weekday()::
        Monday is 0 and Sunday is 6

    .strftime()::
        Return a string representing the time, controlled by an explicit format string.

"""

from datetime import time


if __name__ == '__main__':
    my_time = time(12)
    print(my_time, type(my_time))

    my_time = time(12, 6, 1)
    print(my_time, type(my_time))

    # you can reverse the order using kwargs
    my_time = time(second=1, minute=6, hour=12)
    print(my_time, type(my_time))

    print(my_time.hour, my_time.minute, my_time.second, my_time.microsecond)

    print(my_time.strftime('%H:%M:%S'))
