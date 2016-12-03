
from cherrydo.common import CherryDoGenerator
from cherrydo.configuration import GENERATE_CONTROLLER
from cherrydo.configuration import GENERATE_CONTROLLER_VIEW
from cherrydo.utils import cherrydo_project_name
from cherrydo.utils import read_template
from cherrydo.utils import template_to_file


class GenerateController(CherryDoGenerator):
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
