from tt.dataaccess.utils import get_data_store
from tt.actions.utils.utils import ensure_working


def action_note(colorizer, content):
    data = get_data_store().load()

    ensure_working(data)

    current = data['work'][-1]

    if 'notes' not in current:
        current['notes'] = [content]
    else:
        current['notes'].append(content)

    get_data_store().dump(data)

    print('Yep, noted to ' + colorizer.yellow(current['name']) + '.')
