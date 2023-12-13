import datetime as dt


def getYear() -> int:
    return dt.datetime.max.year


print(getYear())
