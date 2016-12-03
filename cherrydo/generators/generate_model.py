
from cherrydo.common import CherryDoGenerator


class GenerateModel(CherryDoGenerator):
    def create(self):
        print('Creating model: {} - {}'.format(self.model_name, self.params))

        self.validate()
        # context = self.default_context()

        return True
