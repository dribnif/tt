from tt.exceptz.exceptz import NoTask, BadArguments


def ensure_working(data):
    if data.get('work') and 'end' not in data['work'][-1]:
        return

    raise NoTask("For all I know, you aren't working on anything. "
                 "I don't know what to do.\n"
                 "See `tt -h` to know how to start working.")


def ensure_end_after_start(entry, end_time):
    if end_time <= entry['start']:
        raise BadArguments("The task is supposed to end before it has begun or at the same time "
                           "You seem confused. Now I'm confused. Aborting...")
