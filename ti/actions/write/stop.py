from ti.dataaccess.utils import get_data_store
from ti.actions.utils.utils import ensure_working
from ti.dateutils.dateutils import formatted_str_for_isotime_str


def action_stop(colorizer, time):
    data = get_data_store().load()

    ensure_working(data)

    current = data['work'][-1]
    current['end'] = time
    get_data_store().dump(data)

    print('So you stopped working on ' + colorizer.red(current['name']) + ' at ' +
          colorizer.yellow(formatted_str_for_isotime_str(time, '%H:%M')) + '.')
