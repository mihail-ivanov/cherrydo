

from args import get_arg, get_arg_list
from helpers import is_cherrydo_project, cherrydo_project_name


def _generate_controller(controller_name, params):
    print('Creating controller: {}'.format(controller_name))
    print(params)

    if not is_cherrydo_project():
        print('CherryDo project not found!')
        return False

    project_name = cherrydo_project_name()
    print('Project name: {}'.format(project_name))

    return True


def _generate_model(model_name, params):
    print('Creating model: {}'.format(model_name))
    print(params)


def _generate_view(controller_name, view_name):
    print('Creating view: {}-{}'.format(controller_name, view_name))


def check_generate(command):
    if command == 'generate':
        subcommand = get_arg(2)

        if subcommand == 'controller':
            controller_name = get_arg(3)
            if controller_name:
                params = get_arg_list(4)
                _generate_controller(controller_name, params)
                return True

        if subcommand == 'model':
            model_name = get_arg(3)
            if model_name:
                params = get_arg_list(4)
                _generate_model(model_name, params)
                return True

        if subcommand == 'view':
            controller_name = get_arg(3)
            view_name = get_arg(4)
            if controller_name and view_name:
                _generate_view(controller_name, view_name)
                return True

    return False
