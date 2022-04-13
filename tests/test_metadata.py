#!/usr/bin/env python


import provide_dir
import datetime


def test_date():
    provide_dir_date = provide_dir.__release_date__
    assert isinstance(
        provide_dir_date, datetime.date
    ), "__release_date__ must be instance of datetime.date"
    today = datetime.datetime.today()
    assert provide_dir_date.year == today.year, "date.year in `__init__.py` is not current"
    assert provide_dir_date.month == today.month, "date.month in `__init__.py` is not current"
    assert provide_dir_date.day == today.day, "date.day in `__init__.py` is not current"

