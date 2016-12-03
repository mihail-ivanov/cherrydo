
from cherrydo.args import get_arg
from cherrydo.configuration import MANDATORY_DIRECTORIES
from cherrydo.configuration import NEW_CREATE_FILES
from cherrydo.configuration import OPTIONAL_DIRECTORIES
from cherrydo.configuration import REQUIREMENTS
from cherrydo.helpers import change_dir
from cherrydo.helpers import create_dir
from cherrydo.helpers import is_cherrydo_project
from cherrydo.helpers import path_exists
from cherrydo.helpers import template_to_file


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

    # Create requirements file
    template_to_file('requirements.txt', 'requirements.txt', {'libraries': "\n".join(REQUIREMENTS)})

    # Create directories
    for dir_name in MANDATORY_DIRECTORIES + OPTIONAL_DIRECTORIES:
        create_dir(dir_name)

    # Create initial files
    context = {'project_name': project_name}
    for file_info in NEW_CREATE_FILES:
        template_to_file(
            file_info['template_name'],
            file_info['destination'],
            context,
            skip_format=file_info.get('skip_format', False)
        )

    return True


def check_new(command):
    if command == 'new':
        project_name = get_arg(2)
        _new_project(project_name)
        return True

    return False
