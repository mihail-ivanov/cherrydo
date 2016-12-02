
import sys


def get_arg(index):
    if len(sys.argv) > index:
        return sys.argv[index]
    return None


def get_arg_list(start_index):
    params = []
    for index in range(start_index, len(sys.argv)):
        params.append(sys.argv[index])
    return params
