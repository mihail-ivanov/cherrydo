
import sys

from cherrydo.args import get_arg
from cherrydo.db import check_db
from cherrydo.generate import check_generate
from cherrydo.new import check_new


def print_help():
    help_text = """
Usage:
    {0} new <project_name> - Creates new project into the current directory

    {0} generate controller <controller_name> (<params>) - creates new controller with provided views
    {0} generate model <model_name> (<params>) - creates new model with provided fields

    {0} db migrate - creates and executes migrations
    {0} db rollback - rollback the last executed migration
    """
    print(help_text.format(sys.argv[0]))


def run():
    command = get_arg(1)

    if (not check_new(command) and
        not check_generate(command) and
        not check_db(command)):
        print_help()


if __name__ == '__main__':
    run()
