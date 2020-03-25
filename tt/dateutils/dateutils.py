import pytz
import os
import re

from tzlocal import get_localzone
from datetime import datetime, timedelta
from tt.exceptz.exceptz import TIError


TT_TODAY_ENV_VAR = "TT_CURRENT_DAY"

def get_local_timezone():
    return get_localzone()

#   returns a datetime
def utc_to_local(utc_dt):
    local_tz = get_local_timezone()
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)

#   returns a datetime
def isotime_utc_to_local(isotime_utc):
    return utc_to_local(parse_isotime(isotime_utc))


def parse_isotime(isotime_str):
    return datetime.strptime(isotime_str, '%Y-%m-%dT%H:%M:%S.%fZ')

#   returns a datetime for an input string
def to_datetime(timestr):
    return parse_time_h_m_to_iso(timestr).isoformat() + 'Z'


def local_to_utc(local_dt):
    local_dt_dst = get_local_timezone().localize(local_dt)
    utc_dt = local_dt_dst.astimezone(pytz.utc)
    return utc_dt.replace(tzinfo=None)


def formatted_str_for_isotime_str(isotime_str, format_str):
    localtime = isotime_utc_to_local(isotime_str)
    return localtime.strftime(format_str)


def get_current_day():
    today_value = os.getenv(TT_TODAY_ENV_VAR, None)
    return today_value


def get_now():
    return datetime.now()


def parse_time_multiformat(timestr):
    if timestr == "now":
        return get_now()
    for time_format in ["%H:%M", "%H%M"]:
        try:
            settime = datetime.strptime(timestr, time_format)
            return settime
        except Exception as keep_going:
            pass

    raise TIError("Can't parse your date string. Supported formats are 14:30 or 1430")


def get_current_year_local_tz():
    now = datetime.utcnow()
    now_local_dt = utc_to_local(now)
    return now_local_dt.strftime("%Y")


def parse_time_h_m_to_iso(timestr):
    now = datetime.utcnow()
    
    try:
        settime = parse_time_multiformat(timestr)
        x = now.replace(hour=settime.hour, minute=settime.minute, second=0, microsecond=1)
        if get_current_day() is not None:
            currentday = datetime.strptime(get_current_day(), "%Y-%m-%d")
            y = x.replace(day=currentday.day, month=currentday.month, year=currentday.year)
            return local_to_utc(y)
        return local_to_utc(x)
    except Exception as e:
        print(e)

    raise TIError("Don't understand the time %r" % (timestr,))


def timegap(start_time, end_time):
    diff = end_time - start_time

    mins = diff.total_seconds() // 60

    if mins == 0:
        return 'less than a minute'
    elif mins == 1:
        return 'a minute'
    elif mins < 44:
        return '{} minutes'.format(mins)
    elif mins < 89:
        return 'about an hour'
    elif mins < 1439:
        return 'about {} hours'.format(mins // 60)
    elif mins < 2519:
        return 'about a day'
    elif mins < 43199:
        return 'about {} days'.format(mins // 1440)
    elif mins < 86399:
        return 'about a month'
    elif mins < 525599:
        return 'about {} months'.format(mins // 43200)
    else:
        return 'more than a year'
