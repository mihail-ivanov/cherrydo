
from args import get_arg


def _db_migrate():
    pass


def _db_rollback():
    pass


def check_db(command):
    if command == 'db':
        subcommand = get_arg(2)

        if subcommand == 'migrate':
            _db_migrate()
            return True

        if subcommand == 'rollback':
            _db_rollback()
            return True

    return False
