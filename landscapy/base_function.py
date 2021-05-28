import numpy

class BaseFunction:
    """
    """
    def __init__(self, inverted=False):
        self._evaluated = 0
        self.inverted=inverted

    def __call__(self, values):
        """Evaluate function and increment evaluation counter.
        """
        evaluation = self.__evaluate__(values)
        self._evaluated += 1
        if self.inverted:
            evaluation = 1 / (1 + evaluation)

        return evaluation

    def __evaluate__(self, values):

        return 0.0
    
    @property
    def evaluated(self):
        """Return how many times was the function evaluated.
        """
        return self._evaluated
