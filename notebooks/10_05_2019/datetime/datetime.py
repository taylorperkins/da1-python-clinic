"""Datetime!!
Single object containing all the information from a date object and a time object
https://docs.python.org/2/library/datetime.html#datetime-objects

Signature::

    datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
        * Note that "year", "month", and "day" are REQUIRED, others are optional

Main functions::

    .today()::
        Current local datetime

    .now([tz])::
        Current local date and time. Optionally specify timezone

    .utcnow()::
        Return the current UTC date and time

    .strptime(date_string, format)::
        Return a datetime corresponding to date_string, parsed according to format

    .strftime(format)::
        Return a string representing the date and time, controlled by an explicit format string

    .date()::
        Return date object with same year, month and day

    .time()::
        Return time object with same hour, minute, second and microsecond


Fun Operations::

    | V1       | Op       | V2        | Returns
    __________________________________________
    | datetime | -        | timedelta | datetime
    | datetime | +        | timedelta | datetime
    | datetime | (+|-)    | datetime  | timedelta
"""

from datetime import datetime


if __name__ == '__main__':
    today = datetime.today()
    print(today, type(today))

    # this could be more precise than "today()" b/c you can specify timezone
    now = datetime.now()
    print(now, type(now))

    utcnow = datetime.utcnow()
    print(utcnow, type(utcnow))

    # IMPORTANT:: http://strftime.org/

    new_datetime = datetime.strptime('1995-11-17', '%Y-%m-%d')
    print(new_datetime, type(new_datetime))

    new_datetime = datetime.strptime('November 17, 95', '%B %d, %y')
    print(new_datetime, type(new_datetime))

    # crazy date formatting!!
    new_datetime = datetime.strptime("17th of November 1995 at 9PM", '%dth of %B %Y at %I%p')
    print(new_datetime, type(new_datetime))

    # convert it back to a string representation.
    new_datetime_as_str = new_datetime.strftime('%x %X')
    print(new_datetime_as_str, type(new_datetime_as_str))

    my_date = datetime.now().date()
    my_time = datetime.now().time()

    print(my_date, my_time)

    age = datetime.now() - new_datetime
    print(age, type(age))






