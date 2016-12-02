
import os

from cherrydo.configuration import MANDATORY_DIRECTORIES


def get_current_path(path):
    current_dir = os.getcwd()

    if isinstance(path, str):
        return os.path.join(current_dir, path)
    else:
        return os.path.join(current_dir, *path)


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
