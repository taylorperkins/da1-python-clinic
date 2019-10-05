import pandas as pd


seconds = pd.Series([1, 60, 300, 3_600, 43_200, 86_400, 31_536_000])


def minutes(n_seconds):
    return n_seconds // 60


def hours(n_seconds):
    return n_seconds // 60 // 60


def days(n_seconds):
    return n_seconds // 60 // 60 // 24


def years(n_seconds):
    return n_seconds // 60 // 60 // 24 // 365


seconds.apply(minutes)


if __name__ == '__main__':
    seconds = pd.Series([1, 60, 300, 3_600, 43_200, 86_400, 31_536_000])

    # print(seconds.apply(minutes))
    # print(seconds.apply(hours))
    # print(seconds.apply(days))
    # print(seconds.apply(years))
