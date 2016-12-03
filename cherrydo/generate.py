
from cherrydo.args import get_arg
from cherrydo.args import get_arg_list
from cherrydo.generators import GenerateController
from cherrydo.generators import GenerateModel


def check_generate(command):
    if command == 'generate':
        subcommand = get_arg(2)

        if subcommand == 'controller':
            controller_name = get_arg(3)
            if controller_name:
                params = get_arg_list(4)
                controller = GenerateController(controller_name, params)
                controller.create()
                return True

        if subcommand == 'model':
            model_name = get_arg(3)
            if model_name:
                params = get_arg_list(4)
                model = GenerateModel(model_name, params)
                model.create()
                return True

    return False
