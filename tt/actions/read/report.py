from __future__ import print_function

from collections import defaultdict

from tt.dateutils.dateutils import *
from tt.dataaccess.utils import get_data_store
from tt.actions.utils import reportingutils


def action_report(colorizer, activity):
    print('Displaying all entries for ', colorizer.yellow(activity), ' grouped by day:', sep='')
    print()
    sep = ' | '
    data = get_data_store().load()
    work = data['work']
    report = defaultdict(lambda: {'sum': timedelta(), 'notes': '', 'weekday': '', 'start_time': None, 'end_time': None})

    total_time = 0
    for item in work:
        if item['name'] == activity and 'end' in item:
            start_time = parse_isotime(item['start'])
            end_time = parse_isotime(item['end'])
            day = reportingutils.extract_day(item['start'])
            duration = parse_isotime(item['end']) - parse_isotime(item['start'])
            report[day]['sum'] += duration
            report[day]['notes'] += reportingutils.get_notes_from_workitem(item)
            report[day]['weekday'] = reportingutils.extract_day_custom_formatter(item['start'], '%a')
            report[day]['start_time'] = get_min_date(report[day]['start_time'], start_time)
            report[day]['end_time'] = get_max_date(report[day]['end_time'], end_time)
            total_time += duration.seconds

    print('weekday', sep, 'date', sep, 'start time', sep, 'end time', sep, 'break', sep, 'total duration', sep,
          'description', sep)

    for date, details in sorted(report.items()):
        start_time = utc_to_local(details['start_time']).strftime("%H:%M")
        end_time = utc_to_local(details['end_time']).strftime("%H:%M")
        break_duration = get_break_duration(details['start_time'], details['end_time'], details['sum'])
        print(details['weekday'], sep, date, sep, start_time, sep, end_time, sep,
              format_time(break_duration,colorizer), sep, format_time(details['sum'],colorizer), sep, details['notes'], sep="")

    should_hours = 8 * len(report.items())
    should_hours_str = str(should_hours) + ':00'
    print()
    print('Based on your current entries, you should have logged ', colorizer.green(should_hours_str), ' ; you instead logged ',
          format_time_seconds(total_time,colorizer), sep='')


def get_break_duration(start_time, end_time, net_work_duration):
    total_work_duration = end_time - start_time
    return total_work_duration - net_work_duration


def format_time(duration_timedelta, colorizer):
    return format_time_seconds(duration_timedelta.seconds, colorizer)


def format_time_seconds(duration_secs, colorizer):
    hours, rem = divmod(duration_secs, 3600)
    mins, secs = divmod(rem, 60)
    formatted_time_str = str(hours).rjust(2, str('0')) + ':' + str(mins).rjust(2, str('0'))
    if hours >= 8:
        return colorizer.green(formatted_time_str)
    else:
        return colorizer.red(formatted_time_str)


def get_min_date(date_1, date_2):
    if date_1 is None:
        date_1 = parse_isotime('2099-01-01T00:00:00.000001Z')
    return date_1 if date_1 < date_2 else date_2


def get_max_date(date_1, date_2):
    if date_1 is None:
        date_1 = parse_isotime('2015-01-01T00:00:00.000001Z')
    return date_1 if date_1 > date_2 else date_2
