
import os

from cherrydo.args import get_arg
from cherrydo.configuration import MANDATORY_DIRECTORIES, OPTIONAL_DIRECTORIES
from cherrydo.helpers import is_cherrydo_project, path_exists, create_dir, change_dir


def _new_project(project_name):
    print('Creating project: {}'.format(project_name))

    if is_cherrydo_project():
        print('Cannot create project inside another project!')
        return False

    if path_exists(project_name):
        print('Cannot create directory: {}'.format(project_name))
        return False

    create_dir(project_name)
    change_dir(project_name)

    for dir_name in MANDATORY_DIRECTORIES + OPTIONAL_DIRECTORIES:
        create_dir(dir_name)

    return True


def check_new(command):
    if command == 'new':
        project_name = get_arg(2)
        _new_project(project_name)
        return True

    return False
