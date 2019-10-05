
from .lvl_1 import seconds

import pandas as pd


def times_2(value):
    return value * 2


if __name__ == '__main__':
    my_dataframe = pd.DataFrame(
        {
            'seconds': seconds,
            'numbers': [1, 2, 3, 4, 5, 6, 7],
            'letters': ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        }
    )

    print(my_dataframe.apply(seconds))
    print(my_dataframe.apply(seconds, axis=1))
    print(my_dataframe.numbers.apply(seconds))
