
from cherrydo.args import get_arg
from cherrydo.generators import NewProject


def check_new(command):
    if command == 'new':
        project_name = get_arg(2)
        project = NewProject(project_name)
        project.create()
        return True

    return False
