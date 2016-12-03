

from cherrydo.args import get_arg, get_arg_list
from cherrydo.configuration import GENERATE_CONTROLLER
from cherrydo.configuration import GENERATE_VIEW
from cherrydo.configuration import GENERATE_CONTROLLER_VIEW
from cherrydo.helpers import append_template_to_file
from cherrydo.helpers import cherrydo_project_name
from cherrydo.helpers import is_cherrydo_project
from cherrydo.helpers import template_to_file
from cherrydo.helpers import read_template
from cherrydo.helpers import CherryDoException


class NewGenerator(object):
    def __init__(self, name, params):
        self.name = name
        self.params = params

    def formatted_name(self):
        return self.name.replace('_', ' ').title().replace(' ', '')

    def validate(self):
        if not is_cherrydo_project():
            raise CherryDoException('CherryDo project not found!')

    def default_context(self):
        return {}

    def create(self):
        return True


class NewController(NewGenerator):
    def generate_methods(self):
        if self.params:
            method_definitions = []

            for view in self.params:
                template_name = GENERATE_CONTROLLER_VIEW['template_name']

                # Create the controller file
                method_definitions.append(read_template(template_name).format(**{'view_name': view}))

            return ''.join(method_definitions)
        else:
            return 'pass'

    def default_context(self):
        return {
            'project_name': cherrydo_project_name(),
            'controller_name': self.name,
            'controller_name_formatted': self.formatted_name(),
            'methods': self.generate_methods(),
        }

    def create(self):
        print('Creating controller: {} - {}'.format(self.name, self.params))

        self.validate()
        context = self.default_context()

        for file_info in GENERATE_CONTROLLER:
            template_name = file_info['template_name'].format(**context)
            destination = file_info['destination'].format(**context)

            # Create the controller file
            template_to_file(template_name, destination, context)

        return True


class NewModel(NewGenerator):
    def create(self):
        print('Creating model: {} - {}'.format(self.model_name, self.params))

        self.validate()
        context = self.default_context()

        return True


def check_generate(command):
    if command == 'generate':
        subcommand = get_arg(2)

        if subcommand == 'controller':
            controller_name = get_arg(3)
            if controller_name:
                params = get_arg_list(4)
                controller = NewController(controller_name, params)
                controller.create()
                return True

        if subcommand == 'model':
            model_name = get_arg(3)
            if model_name:
                params = get_arg_list(4)
                model = NewModel(model_name, params)
                model.create()
                return True

    return False
