"""
Testing time of day. Use freeze_time.
"""

from freezegun import freeze_time
from unittesting.unittesting.current_time_of_day import time_of_day


@freeze_time("2022-04-29 2:21:58")
def test_night():
    """
    Check time of day NIGHT. From 00.00  until 06.00.
    """
    assert time_of_day() == "night"


@freeze_time("2022-04-29 8:45:12")
def test_night():
    """
    Check time of day MORNING. This time from 6.00 until 12.00
    """
    assert time_of_day() == "morning"


@freeze_time("2022-04-29 15:27:30")
def test_night():
    """
    Check time of day AFTERNOON. This time from 12.00 until 18.00
    """
    assert time_of_day() == "afternoon"


@freeze_time("2022-04-29 21:12:21")
def test_night():
    """
    Check time of day NIGHT. This time 18.00 - 00.00.
    """
    assert time_of_day() == "night"


