import numpy

class BaseFunction:
    """
    """
    def __init__(self, inverted=False):

        self.inverted=inverted

    def __call__(self, values):
        """
        """
        evaluation = self.__evaluate__(values)

        if self.inverted:
            evaluation = 1 / (1 + evaluation)

        return evaluation

    def __evaluate__(self, values):

        return 0.0
