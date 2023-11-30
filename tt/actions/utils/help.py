
def print_help():
    print('tt is a simple command-line time tracking tool.')
    print()
    print('It stores all the information you add in a JSON-formatted time entry database, located  \n'
          'either at the location you specify in the environment variable SHEET_FILE, or by default \n'
          'in ${HOME}/.tt-sheet.json, in case you don\'t set your SHEET_FILE.')
    print()
    print('Usage:')
    print('tt COMMAND [PARAM_0] .. [PARAM_n]')
    print()
    print('Commands: ')
    print('  start [WORK_PACKAGE] [STARTING_TIME] \n'
          '    Description:\n'
          '      Opens a new work package with the supplied name, starting at the supplied time\n'
          '    Examples:\n'
          '      tt start cleaning 10:30\n'
          '      tt start cleaning 1030\n'
          '      tt start cleaning now')
    print()
    print('  stop [END_TIME]\n'
          '    Description:\n'
          '      Closes an open work package at the supplied time\n'
          '    Examples:\n'
          '      tt stop 10:30\n'
          '      tt stop 1030\n'
          '      tt stop now')
    print()
    print('  note [TEXT]\n'
          '    Description:\n'
          '      Adds a note to an open work package\n'
          '    Examples:\n'
          '      tt note x\n'
          '      tt note \'The quick brown fox humps the lazy bear\'')

    print()
    print('  tag [TAG0] [TAG1] [TAG2]\n'
          '    Description:\n'
          '      Adds a list of tags to an open work package\n'
          '    Examples:\n'
          '      tt tag TAGNAME\n'
          '      tt tag \'housework\' \'#makeherproud\'')

    print()
    print('  edit \n'
          '    Description:\n'
          '      Opens your time entry database located at ${SHEET_FILE} on an editor of your choosing. The editor\n'
          '      needs to be specified by setting another environment variable: export EDITOR=\'vim\'\n'
          '      Saving and exiting the editor, updates the time entry db with the new info.\n'
          '      Graphical text editors, such as kate, gedit or sublime ar supported just as well.\n'
          '    Examples:\n'
          '      tt edit')

    print()
    print('  csv \n'
          '    Description:\n'
          '      Lists all your individual entries in a comma-separated format, for ease of import into spreadsheet\n'
          '      editors such as LibreOffice Sheets. The separator is the pipe symbol.\n'
          '    Examples:\n'
          '      tt csv\n'
          '      tt csv --nocolor > /tmp/allentries.csv ; libreoffice /tmp/allentries.csv')

    print()
    print('  status \n'
          '    Description:\n'
          '      Shows all information pertaining to an open work package or an appropriate message, if one cannot\n'
          '      be found. \n'
          '    Examples:\n'
          '      tt status\n'
          '      tt status --nocolor')
    print()
    print('  report [WORK_PACKAGE] \n'
          '    Description:\n'
          '      Creates an aggregated daily report for the work package you specify as parameter. It creates one\n'
          '      aggregated entry per day, based on the entire database content. If you need to restrict the report\n'
          '      to certain periods, such as a specific month, feel free to pipe the output through grep or other\n'
          '      cli tools. If no work package is specified, all activities will be reported.\n'
          '    Examples:\n'
          '      tt report\n'
          '      tt report cleaning\n'
          '      tt report cleaning --nocolor\n'
          '      tt report cleaning --nocolor | grep 2019-03 ')
    print()
    print('  log [START_DATETIME] [END_DATETIME] \n'
          '    Description:\n'
          '      Prints a log of the total time spent on each activity, optionally filtered by activities started\n'
          '      within a given time period\n'
          '    Examples:\n'
          '      tt log\n'
          '      tt log 2023-11-13\n'
          '      tt log 2023-11-13 2023-11-15T13:00:00')
    print()
    print('  calview [MONTH] [YEAR] \n'
          '    Description:\n'
          '      Renders a monthly workday calendar (Monday-Friday) with daily aggregated package durations.\n'
          '      The [YEAR] parameter is optional; if omitted, it defaults to the current year. \n'
          '    Examples:\n'
          '      tt calview 12\n'
          '      tt calview 11 --nocolor\n'
          '      tt calview 10 2030')
    print()
    print('For the full documentation, check out http://github.com/dribnif/tt')
