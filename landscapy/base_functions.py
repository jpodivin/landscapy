import numpy as np


class BaseFunction:
    """Base class of test functions.
    """
    def __init__(self, inverted=False):
        self._evaluated = 0
        self.inverted = inverted

    def __call__(self, values):
        """Evaluate function and increment evaluation counter.
        """
        evaluation = self.__evaluate__(values)
        self._evaluated += 1
        if self.inverted:
            evaluation = 1 / (1 + evaluation)

        return evaluation

    def __evaluate__(self, values):
        """Evaluate the function at a given point.
        Return results.
        :param values: function input
        :type values: numpy array

        :rtype: float
        """
        return 0.0

    @property
    def evaluated(self):
        """Return how many times was the function evaluated.
        """
        return self._evaluated


class SquashedDimsFunction(BaseFunction):

    def __init__(self, inverted, final_dimension, strategy='splitsum'):
        self._final_dimension = final_dimension
        self._squash_strategy = strategy
        super().__init__(inverted=inverted)

    def __call__(self, values):
        if self._squash_strategy == 'splitsum':
            values = np.reshape(values, (self._final_dimension, -1))
            values = np.sum(values, 1)
        return super().__call__(values)
