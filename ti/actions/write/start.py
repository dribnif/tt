from ti.exceptz.exceptz import AlreadyOn
from ti.dataaccess.utils import get_data_store
from ti.dateutils.dateutils import formatted_str_for_isotime_str

def action_start(colorizer, name, time):
    data = get_data_store().load()
    work = data['work']

    if work and 'end' not in work[-1]:
        raise AlreadyOn("You are already working on %s. Stop it or use a "
                        "different sheet." % (colorizer.yellow(work[-1]['name']),))

    entry = {
        'name': name,
        'start': time,
    }

    work.append(entry)
    get_data_store().dump(data)

    print('Started working on ' + colorizer.green(name) + ' at ' +
           colorizer.yellow(formatted_str_for_isotime_str(time, '%H:%M')) + '.')
