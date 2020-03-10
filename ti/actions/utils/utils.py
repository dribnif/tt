from ti.exceptz.exceptz import NoTask


def ensure_working(data):
    if data.get('work') and 'end' not in data['work'][-1]:
        return

    raise NoTask("For all I know, you aren't working on anything. "
                 "I don't know what to do.\n"
                 "See `ti -h` to know how to start working.")
