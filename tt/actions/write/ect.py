import yaml
import os
import tempfile
import subprocess

from tt.actions.utils.utils import ensure_working
from tt.exceptz.exceptz import InvalidYAML
from tt.exceptz.exceptz import NoEditor
from tt.dataaccess.utils import get_data_store


def action_edit_current_timebox():
    if "EDITOR" not in os.environ:
        raise NoEditor("Please set the 'EDITOR' environment variable")

    store = get_data_store()
    data = store.load()

    ensure_working(data)

    current = data['work'][-1]
    current_notes = [''] if 'notes' not in current else current['notes']

    the_yml = yaml.safe_dump(current_notes, default_flow_style=False, allow_unicode=True)

    cmd = os.getenv('EDITOR')
    fd, temp_path = tempfile.mkstemp(suffix='.yml', prefix='tt-current-timebox-edit.')

    with open(temp_path, "r+") as f:
        f.write("#you are editing the current timebox: " + current['name'] + "\n")
        f.write("#beginning: " + current['start'][:-8] + "\n" )
        f.write(the_yml)
        f.seek(0)
        subprocess.check_call(cmd + ' ' + temp_path, shell=True)
        the_yml = f.read()
        f.truncate()
        f.close

    os.close(fd)
    os.remove(temp_path)

    try:
        current_notes_from_yml = yaml.load(the_yml, Loader=yaml.SafeLoader)
        current['notes'] =  current_notes_from_yml
    except yaml.YAMLError as exc:
        raise InvalidYAML("Oops, that YAML doesn't appear to be valid!")

    store.dump(data)
