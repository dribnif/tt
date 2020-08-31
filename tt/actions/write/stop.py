from tt.dataaccess.utils import get_data_store
from tt.actions.utils.utils import ensure_working
from tt.actions.utils.utils import ensure_end_after_start
from tt.dateutils.dateutils import formatted_str_for_isotime_str


def action_stop(colorizer, time):
    data = get_data_store().load()

    ensure_working(data)
    current_entry = data['work'][-1]

    ensure_end_after_start(current_entry, time)
    current_entry['end'] = time

    get_data_store().dump(data)

    print('You stopped working on ' + colorizer.red(current_entry['name']) + ' at ' +
          colorizer.yellow(formatted_str_for_isotime_str(time, '%H:%M')) + '.')
