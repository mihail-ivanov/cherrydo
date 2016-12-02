
import os

from cherrydo.configuration import MANDATORY_DIRECTORIES


def get_current_path(path):
    current_dir = os.getcwd()

    if isinstance(path, str):
        return os.path.join(current_dir, path)
    else:
        return os.path.join(current_dir, *path)


def get_cherrydo_lib_path(path):
    dir_path = os.path.dirname(os.path.abspath(__file__))

    if isinstance(path, str):
        return os.path.join(dir_path, path)
    else:
        return os.path.join(dir_path, *path)


def is_cherrydo_project():
    for dir_path in MANDATORY_DIRECTORIES:
        if not os.path.isdir(get_current_path(dir_path)):
            return False
    return True


def cherrydo_project_name():
    if is_cherrydo_project():
        return os.path.dirname(os.getcwd())
    return None


def change_dir(path):
    os.chdir(get_current_path(path))


def path_exists(path):
    return os.path.exists(get_current_path(path))


def create_dir(path):
    os.makedirs(get_current_path(path))


def read_template(template_name):
    file_path = get_cherrydo_lib_path(['templates', template_name])
    data = None
    with open(file_path, 'r') as tfile:
        data = tfile.read()
    return data


def template_to_filename(template_name):
    return template_name.replace('.pystr', '')

