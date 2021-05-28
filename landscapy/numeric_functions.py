from landscapy import base_functions as bf
import numpy as np


class SphereFn(bf.BaseFunction):
    """Sum of squares. N-dimensional
    """
    def __init__(self, inverted):
        super().__init__(inverted=inverted)

    def __evaluate__(self, values):
        result = np.sum(np.power(values, 2))

        return result

    def _optima(self, values):
        if all([i == 0 for i in values]):
            return 0
        else:
            raise ValueError

class StyblinskiTangFn(bf.BaseFunction):
    """Styblinski–Tang function. N-dimensional
    """
    def __init__(self, inverted):

        super().__init__(inverted=inverted)

    def __evaluate__(self, values):
        result = np.power(values, 4) - 16 * np.power(values, 2) + 5 * values
        result = np.sum(result)

        return result

    def _optima(self, values):
        if all([i==2.903534 for i in values]):
            return -39.16599
        else:
            raise ValueError

class HappyCatFn(bf.BaseFunction):
    """Happy cat function.
    Hans-Georg Beyer, Steffen Finck:
    HappyCat – A Simple Function Class Where Well-Known Direct Search Algorithms Do Fail
    (2012)
    """
    def __init__(self, inverted=False, alpha=1/8):
        self.alpha = alpha

        super(HappyCatFn, self).__init__(inverted=inverted)

    def __evaluate__(self, values):
        norm = np.linalg.norm(values)
        result = np.power(norm, 2) - values.size
        result = np.power(np.power(result, 2), self.alpha)
        result += (1/values.size) * (0.5 * np.power(norm, 2) + np.sum(values))
        result += 0.5

        return result

    def _optima(self, values):
        if all([i == -1 for i in values]):
            0.0
        else:
            raise ValueError

class ShwefelFn(bf.BaseFunction):
    """Schwefel 2.20 Function
    """
    def __evaluate__(self, values):
        result = np.abs(values)
        result = np.sum(result)

        return result


class HolderTableFn(bf.SquashedDimsFunction):
    """Holder Table function. 2-dimensional
    """
    def __init__(self, inverted=False):

        super().__init__(inverted, 2)

    def __evaluate__(self, values):

        x = values[0]
        y = values[1]

        result = np.sqrt(np.power(x, 2) + np.power(y, 2))
        result = np.abs(1 - (result / np.pi))
        result = np.sin(x) * np.cos(y) * np.exp(result)
        result = -np.abs(result)

        return result

    def _optima(self, values):
        min_dict = {
            (8.05502, 9.66459): -19.2085,
            (8.05502, -9.66459): -19.2085,
            (-8.05502, -9.66459): -19.2085,
            (-8.05502, 9.66459): -19.2085,
        }

        return min_dict.get(tuple(values))