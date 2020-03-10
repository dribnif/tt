import os

from ti.datasources.jsondatasource import JsonStore
from ti.exceptz.exceptz import NonexistentDatasource

default_datasource_type = 'JSON'

json_default_env_var_name = 'SHEET_FILE'
json_default_db_location = '~/.tt-sheet.json'


def get_data_store(type=default_datasource_type):
    if type == "JSON":
        return JsonStore(os.getenv(json_default_env_var_name, None) or
                  os.path.expanduser(json_default_db_location))
    else:
        raise NonexistentDatasource('App only supports JSON datasources at the moment')
