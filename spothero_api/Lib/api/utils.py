import calendar
import datetime
import pytz
from dateutil import parser
from .constants import DEFAULT_TIMEZONE


def normalize_date(list_of_days):
    days = list_of_days.split(",")
    days_to_return = []
    for day in days:
        for weekday in calendar.day_name:
            if day in weekday.lower():
                days_to_return.append(weekday.lower())
                break

    return days_to_return


def normalize_tz(time, tz):
    old_timezone = pytz.timezone(tz)
    new_timezone = pytz.timezone(DEFAULT_TIMEZONE)
    new_timezone_timestamp = old_timezone.localize(time).astimezone(new_timezone)
    return new_timezone_timestamp.time(), DEFAULT_TIMEZONE


def military_time_to_standard_time(military_time, time_format):
    hour = ""
    minute = ""
    for i in range(len(time_format)):
        if time_format[i] == "H":
            hour += military_time[i]
        if time_format[i] == "M":
            minute += military_time[i]

    is_pm = False

    if hour > "12":
        int_hour = int(hour)
        int_hour -= 12
        hour = int_hour

        if hour < 10:
            hour = f"0{int_hour}"

        is_pm = True

    if is_pm:
        time = f'{hour}:{minute}:00 PM'
    else:
        time = f'{hour}:{minute}:00 AM'

    return time


def normalize_times(list_of_times, tz):
    times = list_of_times.split("-")
    times_to_return = []
    for time in times:
        standard_time = military_time_to_standard_time(time, "HHMM")
        dt = datetime.datetime.strptime(standard_time, "%I:%M:%S %p")
        normalized_time, tz = normalize_tz(dt, tz)
        times_to_return.append(normalized_time)

    return times_to_return, tz


def get_days_and_times_from_date(start_date, end_date):
    start = parser.parse(start_date)
    end = parser.parse(end_date)
    start_day = calendar.day_name[start.weekday()]
    end_day = calendar.day_name[end.weekday()]
    day = start_day.lower()

    if start_day != end_day:
        day = False

    return day, start.time(), end.time()
