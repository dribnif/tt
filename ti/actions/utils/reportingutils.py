from ti.dateutils.dateutils import *


def get_notes_from_workitem(item):
    notes = ''
    if 'notes' in item:
        for note in item['notes']:
            notes += note + ' ; '
    return notes


def extract_day_custom_formatter(datetime_local_tz, format_string):
    local_dt = isotime_utc_to_local(datetime_local_tz)
    return local_dt.strftime(format_string)


def extract_day(datetime_local_tz):
    return extract_day_custom_formatter(datetime_local_tz, '%Y-%m-%d')


def remove_seconds(timedelta):
    return ':'.join(str(timedelta).split(':')[:2])


