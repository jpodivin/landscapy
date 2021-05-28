from landscapy import base_functions as bf
import numpy as np


class SphereFn(bf.BaseFunction):
    """
    """
    def __evaluate__(self, values):
        result = np.sum(np.power(values, 2))

        return result


class StyblinskiTangFn(bf.BaseFunction):
    """
    """
    def __evaluate__(self, values):
        result = np.power(values, 4) - 16 * np.power(values, 2) + 5 * values
        result = np.sum(result)

        return result


class HappyCatFn(bf.BaseFunction):
    """
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


class ShwefelFn(bf.BaseFunction):
    """Schwefel 2.20 Function
    """
    def __evaluate__(self, values):
        result = np.abs(values)
        result = np.sum(result)

        return result


class QuarticFn(bf.SquashedDimsFunction):
    """Quartic function. Two variable
    """
    def __init__(self, inverted=False):
        super(QuarticFn, self).__init__(inverted, 2)

    def __evaluate__(self, values):
        result = np.pow(values[0], 4)/4 + np.pow(values[0], 2)/2
        result += values[0]/10 + np.pow(values[1], 2)/2

        return result


class HolderTableFn(bf.SquashedDimsFunction):
    """
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
