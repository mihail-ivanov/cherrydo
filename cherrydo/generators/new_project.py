
from cherrydo.common import BaseGenerator
from cherrydo.common import CherryDoException
from cherrydo.configuration import MANDATORY_DIRECTORIES
from cherrydo.configuration import NEW_CREATE_FILES
from cherrydo.configuration import OPTIONAL_DIRECTORIES
from cherrydo.configuration import REQUIREMENTS
from cherrydo.utils import change_dir
from cherrydo.utils import create_dir
from cherrydo.utils import is_cherrydo_project
from cherrydo.utils import path_exists
from cherrydo.utils import template_to_file


class NewProject(BaseGenerator):
    def __init__(self, name):
        super(NewProject, self).__init__(name, {})

    def validate(self):
        if is_cherrydo_project():
            raise CherryDoException('Cannot create project inside another project!')

        if path_exists(self.name):
            raise CherryDoException('Cannot create directory: {}'.format(self.name))

    def default_context(self):
        return {
            'project_name': self.name,
        }

    def create(self):
        print('Creating project: {}'.format(self.name))

        self.validate()

        create_dir(self.name)
        change_dir(self.name)

        # Create requirements file
        template_to_file('requirements.txt', 'requirements.txt', {'libraries': "\n".join(REQUIREMENTS)})

        # Create directories
        for dir_name in MANDATORY_DIRECTORIES + OPTIONAL_DIRECTORIES:
            create_dir(dir_name)

        # Create initial files
        context = self.default_context()

        for file_info in NEW_CREATE_FILES:
            template_to_file(
                file_info['template_name'],
                file_info['destination'],
                context,
                skip_format=file_info.get('skip_format', False)
            )

        return True
