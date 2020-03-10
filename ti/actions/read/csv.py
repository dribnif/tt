from __future__ import print_function

from ti.dataaccess.utils import get_data_store
from ti.dateutils.dateutils import *
from ti.actions.utils import reportingutils


def action_csv():
    sep = '|'
    data = get_data_store().load()
    work = data['work']

    for item in work:
        if 'end' in item:
            notes = reportingutils.get_notes_from_workitem(item)
            duration = parse_isotime(item['end']) - parse_isotime(item['start'])
            duration_total = reportingutils.remove_seconds(duration)
            date = reportingutils.extract_day(item['start'])
            name = item['name']
            start = format_csv_time(item['start'])
            end = format_csv_time(item['end'])
            tags = ''
            if 'tags' in item:
                tags = item['tags']
            print_elements(date, name, start, end, duration_total, notes, tags, sep)


def print_elements(date, name, start, end, total_duration, notes, tags, sep):
    # print(date, sep, name, sep, start, sep, end, sep, total_duration, sep, tags, sep, notes)
    print(date, sep, start, sep, end, sep, '', sep, notes, sep, name)


def format_csv_time(somedatetime):
    local_dt = isotime_utc_to_local(somedatetime)
    return local_dt.strftime('%H:%M')
