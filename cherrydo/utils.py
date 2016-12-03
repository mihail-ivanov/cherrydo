
import os

from cherrydo.configuration import MANDATORY_DIRECTORIES


def get_current_path(path):
    current_dir = os.getcwd()
    return os.path.join(current_dir, *path.split('/'))


def get_cherrydo_lib_path(path):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir_path, *path.split('/'))


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


def create_dir(path, raise_error=True):
    if not os.path.isabs(path):
        path = get_current_path(path)

    print('Creating directory: {}'.format(path))
    try:
        os.makedirs(path)
    except (OSError, FileExistsError):
        if raise_error:
            raise


def read_template(template_name):
    file_path = get_cherrydo_lib_path('templates/{}'.format(template_name))
    data = None
    with open(file_path, 'r') as tfile:
        data = tfile.read()
    return data


def template_to_file(template_name, destination, context, skip_format=False):
    template = read_template(template_name)
    destination_path = get_current_path(destination)
    # Ensure directory
    create_dir(os.path.dirname(destination_path), raise_error=False)

    print('Creating template: {}'.format(destination_path))
    with open(destination_path, 'w') as dfile:
        if skip_format:
            dfile.write(template)
        else:
            dfile.write(template.format(**context))
