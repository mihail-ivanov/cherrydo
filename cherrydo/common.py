
from cherrydo.utils import is_cherrydo_project


class CherryDoException(Exception):
    pass


class BaseGenerator(object):
    def __init__(self, name, params):
        self.name = name
        self.params = params

    def formatted_name(self):
        return self.name.replace('_', ' ').title().replace(' ', '')

    def validate(self):
        pass

    def default_context(self):
        return {}

    def create(self):
        return True


class CherryDoGenerator(BaseGenerator):
    def validate(self):
        if not is_cherrydo_project():
            raise CherryDoException('CherryDo project not found!')
