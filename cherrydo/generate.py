

from cherrydo.args import get_arg, get_arg_list
from cherrydo.configuration import GENERATE_CONTROLLER
from cherrydo.configuration import GENERATE_VIEW
from cherrydo.configuration import GENERATE_CONTROLLER_VIEW
from cherrydo.helpers import append_template_to_file
from cherrydo.helpers import cherrydo_project_name
from cherrydo.helpers import is_cherrydo_project
from cherrydo.helpers import template_to_file
from cherrydo.helpers import read_template


def _format_controller_name(controller_name):
    return controller_name.replace('_', ' ').title().replace(' ', '')


def _generate_controller_methods(controller_name, views):
    if views:
        method_definitions = []

        for view in views:
            template_name = GENERATE_CONTROLLER_VIEW['template_name']

            # Create the controller file
            method_definitions.append(read_template(template_name).format(**{'view_name': view}))

        return ''.join(method_definitions)
    else:
        return 'pass'


def _generate_controller(controller_name, params):
    print('Creating controller: {}'.format(controller_name))
    print(params)

    if not is_cherrydo_project():
        print('CherryDo project not found!')
        return False

    context = {
        'project_name': cherrydo_project_name(),
        'controller_name': controller_name,
        'controller_name_formatted': _format_controller_name(controller_name),
        'methods': _generate_controller_methods(controller_name, params)
    }

    for file_info in GENERATE_CONTROLLER:
        template_name = file_info['template_name'].format(**context)
        destination = file_info['destination'].format(**context)

        # Create the controller file
        template_to_file(template_name, destination, context)

    return True


def _generate_model(model_name, params):
    print('Creating model: {}'.format(model_name))
    print(params)


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

    return False
