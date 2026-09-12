from __future__ import print_function

import textwrap
from datetime import datetime, timedelta
from tt.dataaccess.utils import get_data_store
from tt.dateutils.dateutils import parse_isotime, isotime_utc_to_local, get_now
from tt.actions.utils import reportingutils


def action_day(colorizer, target_date_str=None):
    # Default to today's date in the local timezone if none is provided
    if target_date_str is None:
        target_date_str = get_now().strftime("%Y-%m-%d")

    data = get_data_store().load()
    work = data.get('work', [])

    day_entries = []
    total_duration = timedelta()

    for item in work:
        item_day = reportingutils.extract_day(item['start'])

        if item_day == target_date_str:
            start_dt = parse_isotime(item['start'])
            local_start = isotime_utc_to_local(item['start'])
            start_display = local_start.strftime("%H:%M")

            if 'end' in item:
                end_dt = parse_isotime(item['end'])
                local_end = isotime_utc_to_local(item['end'])
                stop_display = local_end.strftime("%H:%M")
                duration = end_dt - start_dt
            else:
                duration = datetime.utcnow() - start_dt
                stop_display = "NOW  "

            total_duration += duration

            # Fetch notes (no longer truncating)
            notes = reportingutils.get_notes_from_workitem(item).strip()

            day_entries.append({
                'start_dt': local_start,
                'start': start_display,
                'stop': stop_display,
                'duration': _format_timedelta(duration),
                'project': item['name'],
                'notes': notes
            })

    # --- Terminal Rendering ---

    # calview is 136 chars wide. 75% is ~102 chars.
    TOTAL_WIDTH = 102
    PREFIX_WIDTH = 44  # 13 (Time) + 3 + 7 (Dur) + 3 + 15 (Proj) + 3
    NOTE_WIDTH = TOTAL_WIDTH - PREFIX_WIDTH

    today_str = get_now().strftime("%Y-%m-%d")
    title_suffix = " (Today)" if target_date_str == today_str else ""

    print("\n\U0001F4C5 {0}{1}".format(target_date_str, title_suffix))
    print("-" * TOTAL_WIDTH)

    if not day_entries:
        print("No entries found for this date.")
    else:
        # Sort chronologically
        day_entries.sort(key=lambda x: x['start_dt'])

        for e in day_entries:
            time_range = "{0} - {1}".format(e['start'], e['stop'])
            duration_str = "[{0}]".format(e['duration'])

            # Use ljust up to 15 chars. If a project name is longer, we truncate it
            # slightly here so it doesn't break the column layout for notes.
            proj_display = e['project'] if len(e['project']) <= 15 else e['project'][:13] + ".."
            project_str = proj_display.ljust(15)

            time_col = colorizer.yellow(time_range)
            dur_col = colorizer.cyan(duration_str)
            proj_col = colorizer.green(project_str)

            if not e['notes']:
                # No notes to wrap, just print the line
                print("{0}   {1}   {2}".format(time_col, dur_col, proj_col))
                continue

            # Wrap notes to fit the remaining width
            wrapped_notes = textwrap.wrap(e['notes'], width=NOTE_WIDTH)

            # Print the first line with all the prefix data
            first_note_col = colorizer.grey(wrapped_notes[0])
            print("{0}   {1}   {2}   {3}".format(time_col, dur_col, proj_col, first_note_col))

            # If notes overflowed, print subsequent lines with an empty prefix block
            if len(wrapped_notes) > 1:
                empty_prefix = " " * PREFIX_WIDTH
                for line in wrapped_notes[1:]:
                    print("{0}{1}".format(empty_prefix, colorizer.grey(line)))

    print("-" * TOTAL_WIDTH)
    total_logged_str = colorizer.cyan(_format_timedelta(total_duration))
    print("Total Logged:   [{0}]\n".format(total_logged_str))


def _format_timedelta(td):
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return "{0:02d}:{1:02d}".format(hours, minutes)