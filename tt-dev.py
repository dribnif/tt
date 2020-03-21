# coding: utf-8
from __future__ import print_function

import sys

from tt.colors.colors import Colorizer

from tt.dateutils.dateutils import to_datetime

from tt.exceptz.exceptz import BadArguments
from tt.exceptz.exceptz import TIError

from tt.actions.write import edit
from tt.actions.write import start
from tt.actions.write import stop
from tt.actions.write import tag
from tt.actions.write import note

from tt.actions.read import log
from tt.actions.read import csv
from tt.actions.read import report
from tt.actions.read import calview
from tt.actions.read import status


def parse_args(argv=sys.argv):

    colorizer = Colorizer(True)
    if '--no-color' in argv:
        colorizer.set_use_color(False)
        argv.remove('--no-color')

    # prog = argv[0]
    if len(argv) == 1:
        raise BadArguments("You must specify a command.")

    head = argv[1]
    tail = argv[2:]

    if head in ['-h', '--help', 'h', 'help']:
        raise BadArguments()

    elif head in ['edit']:
        fn = edit.action_edit
        args = {}

    elif head in ['start']:
        if not tail or len(tail) != 2:
            raise BadArguments(
                'Please provide a name for the activity and the start time, like so:\n$ tt start project 14:15')

        fn = start.action_start
        args = {
            'colorizer': colorizer,
            'name': tail[0],
            'time': to_datetime(' '.join(tail[1:])),
        }

    elif head in ['stop']:
        fn = stop.action_stop
        args = {'colorizer': colorizer, 'time': to_datetime(' '.join(tail))}

    elif head in ['status']:
        fn = status.action_status
        args = {'colorizer': colorizer}

    elif head in ['log']:
        fn = log.action_log
        args = {'period': tail[0] if tail else None}

    elif head in ['csv']:
        fn = csv.action_csv
        args = {}

    elif head in ['report']:
        fn = report.action_report
        if not tail:
            raise BadArguments('Please provide the name of the activity for which to generate the report')
        args = {'colorizer': colorizer, 'activity': tail[0]}
        
    elif head in ['calview']:
        fn = calview.action_calview
        if not tail:
            raise BadArguments(
                'Please provide the month [optionally followed by the year] for which to generate the activity report')
        args = {'colorizer': colorizer, 'month': tail[0], 'year': tail[1] if len(tail) > 1 else None}

    elif head in ['tag']:
        if not tail:
            raise BadArguments("Please provide at least one tag to add.")

        fn = tag.action_tag
        args = {'tags': tail}

    elif head in ['note']:
        if not tail:
            raise BadArguments("Please provide some text to be noted.")

        fn = note.action_note
        args = {'colorizer': colorizer, 'content': ' '.join(tail)}

    else:
        raise BadArguments("I don't understand %r" % (head,))

    return fn, args


def main():
    try:
        fn, args = parse_args()
        fn(**args)
    except TIError as e:
        msg = str(e) if len(str(e)) > 0 else __doc__
        print(msg, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
