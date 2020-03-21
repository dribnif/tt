from tt.dataaccess.utils import get_data_store
from tt.actions.utils.utils import ensure_working


def action_tag(tags):
    data = get_data_store().load()

    ensure_working(data)

    current = data['work'][-1]

    current['tags'] = set(current.get('tags') or [])
    current['tags'].update(tags)
    current['tags'] = list(current['tags'])

    get_data_store().dump(data)

    tag_count = len(tags)
    print("Okay, tagged current work with %d tag%s."
          % (tag_count, "s" if tag_count > 1 else ""))
