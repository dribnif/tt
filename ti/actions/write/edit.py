import yaml
import os
import tempfile
import subprocess

from ti.exceptz.exceptz import InvalidYAML
from ti.exceptz.exceptz import NoEditor
from ti.dataaccess.utils import get_data_store


def action_edit():
    if "EDITOR" not in os.environ:
        raise NoEditor("Please set the 'EDITOR' environment variable")

    store = get_data_store()

    data = store.load()
    yml = yaml.safe_dump(data, default_flow_style=False, allow_unicode=True)

    cmd = os.getenv('EDITOR')
    fd, temp_path = tempfile.mkstemp(suffix='.yml', prefix='ti.')
    with open(temp_path, "r+") as f:
        f.write(yml.replace('\n- ', '\n\n- '))
        f.seek(0)
        subprocess.check_call(cmd + ' ' + temp_path, shell=True)
        yml = f.read()
        f.truncate()
        f.close

    os.close(fd)
    os.remove(temp_path)

    try:
        data = yaml.load(yml)
    except:
        raise InvalidYAML("Oops, that YAML doesn't appear to be valid!")

    store.dump(data)
