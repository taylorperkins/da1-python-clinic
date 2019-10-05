"""Date!!
represents a date (year, month and day) in an idealized calendar
https://docs.python.org/2/library/datetime.html#date-objects

Signature::

    datetime.date(year, month, day)
        * Note that all arguments are "required", and it doesnt know how to handle times


Main attributes::

    .year::
        year as a number

    .month::
        month as a number

    .day::
        day as a number


Main methods::

    .replace([year [, month] [, day]])::
        Replace one of the values you specify

    .weekday()::
        Monday is 0 and Sunday is 6

    .strftime()::
        Return a string representing the date, controlled by an explicit format string.
        Format codes referring to hours, minutes or seconds will see 0 values


Fun Operations::

    | V1        | Op       | V2        | Returns
    __________________________________________
    | date      | -        | timedelta | date
    | date      | +        | timedelta | date
    | date      | (-|+)    | date      | timedelta
    | date      | <        | date      | bool
"""

from datetime import date


if __name__ == '__main__':
    my_date = date(2017, 11, 1)
    print(my_date, type(my_date))
    print(my_date.year, my_date.month, my_date.day)
    print(my_date.weekday())


