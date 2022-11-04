from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import calendar

from collections import defaultdict

from tt.dateutils.dateutils import *
from tt.dataaccess.utils import get_data_store
from tt.actions.utils import reportingutils
def action_calview(colorizer, month, year):
    report = generate_day_based_report()
    year =  get_current_year_local_tz() if year is None else year

    print('Displaying all entries for ', colorizer.yellow(year+'-'+month),  ' grouped by day:', sep='')

    month_cal = calendar.monthcalendar(int(year),int(month))

    # "normal" beeings don't work on weekends (isSevenDayWeek = false default),
    # in case you like working on saturdays or sundays calview will determine if something was logged
    # if that's the case print the Weekend also in calview, else stay sane with Monday till Friday
    isSevenDayWeek = bool(False)
    for week in range(len(month_cal)):
        weekdays = month_cal[week]
        activity_saturday = get_activity(report, 0, weekdays[5], year, month)
        activity_sunday = get_activity(report, 0, weekdays[6], year, month)
        if activity_saturday != "" or activity_sunday != "":
            isSevenDayWeek = bool(True)

    header = "|         " + colorizer.yellow("Monday") + "           |         " + colorizer.yellow(
        "Tuesday") + "          |         " + colorizer.yellow("Wednesday") + "        |         " + colorizer.yellow(
        "Thursday") + "         |           " + colorizer.yellow("Friday") + "         |"
    delimiter = "+--------------------------+--------------------------+--------------------------+--------------------------+--------------------------+"
    weekEnd = 5

    if (isSevenDayWeek):
        header += "          " + colorizer.yellow("Saturday") + "        |           " + colorizer.yellow(
            "Sunday") + "         |"
        delimiter += "--------------------------+--------------------------+"
        weekEnd = 7

    print(delimiter)
    print(header)
    print(delimiter)
    for week in range(len(month_cal)):
        weekdays = month_cal[week]
        #skip empty weeks completely
        if weekdays[0] == 0 and weekdays[weekEnd - 1] == 0:
            continue
        print("",  end="|")
        for day_index in range(len(weekdays[0:weekEnd])):
            day_cell_header=""
            if weekdays[day_index] != 0:
                day_cell_header=" "+ str(year)+"-"+month.zfill(2)+"-"+str(weekdays[day_index]).zfill(2)
            print(colorizer.blue(day_cell_header.ljust(26, ' ')),  end="|")
        print()
        print(delimiter)
        print_week_activity(colorizer, weekdays[0:weekEnd],  5,  report,  year,  month)
        #print("WEEK DONE")
        print(delimiter)
        

def print_week_activity(colorizer, current_week,  height_in_rows,  report,  year,  month):
   for curr_row in range(height_in_rows):
       print_activity_at_index(colorizer, curr_row,  current_week, report,  year,  month)
       print("") #one week row done

def print_activity_at_index(colorizer, curr_row,  current_week,  report,  year,  month):
    print("",  end="|")    
    for day_index in range(len(current_week)):
        if current_week[day_index] == 0:
            print("".rjust(26, ' '),  end="|")
        else:
            activity_str =  get_activity(report,  curr_row, current_week[day_index],  year,  month)
            print(colorizer.green(activity_str.rjust(26, ' ')),  end="|")

def get_activity(report,  curr_row,  day_key,  year,  month):
    report_key=str(year)+"-"+month.zfill(2)+"-"+str(day_key).zfill(2)
    activity = ""
    try:
        activity_dict = report[report_key]
        if curr_row < len(list(activity_dict)):
            activity_key = list(activity_dict)[curr_row]
            activity_duration = report[report_key][activity_key]
            activity = activity_key + " : " + format_time(activity_duration) + " "
    finally:
        return activity

def generate_day_based_report():
    data = get_data_store().load()
    work = data['work']
    report = dict()
    for item in work:
        day = reportingutils.extract_day(item['start'])
        end_time = parse_isotime(item['end']) if 'end' in item else datetime.utcnow()
        duration = end_time - parse_isotime(item['start'])
        try:
            report[day]
        except KeyError:
            report[day] = defaultdict(lambda: timedelta())

        item_name = item['name'] if 'end' in item else "~wip~" + item['name']
        report[day][item_name] += duration
        #print ('report[', day,  "][", item['name'], "]=" ,  report[day][item['name']])
    return report

def format_time(duration_timedelta):
    return format_time_seconds(duration_timedelta.seconds)


def format_time_seconds(duration_secs ):
    hours, rem = divmod(duration_secs, 3600)
    mins, secs = divmod(rem, 60)
    formatted_time_str = str(hours).rjust(2, str('0')) + ':' + str(mins).rjust(2, str('0'))
    return formatted_time_str
    
