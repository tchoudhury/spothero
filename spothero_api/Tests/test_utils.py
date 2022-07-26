import spothero_api.Lib.api.utils as utils
import datetime


def test_normalize_date():
    list_of_days = "mon,tues,wed,thur,fri,sat,sun"
    normalized_days = utils.normalize_date(list_of_days)

    assert normalized_days[0] == "monday"


def test_normalize_tz():
    dt = datetime.datetime.strptime("09:00:00", "%H:%M:%S")
    tz = "America/New_York"

    normalized_tz, tz = utils.normalize_tz(dt,tz)

    assert tz == "America/Chicago"
    assert normalized_tz == datetime.time(8, 5)


def test_military_time_to_standard_time():
    military_time = "2230"
    time_format = "HHMM"
    time = utils.military_time_to_standard_time(military_time, time_format)

    assert time == "10:30:00 PM"


def test_get_days_and_times_from_date():
    start_date = "2015-07-01T07:00:00-05:00"
    end_date = "2015-07-01T12:00:00-05:00"

    day, start_time, end_time = utils.get_days_and_times_from_date(start_date, end_date)

    assert day == "wednesday"
    assert start_time == datetime.time(7, 0)
    assert end_time == datetime.time(12, 0)
