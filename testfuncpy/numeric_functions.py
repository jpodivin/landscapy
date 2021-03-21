from testfuncpy.base_function import BaseFunction
import numpy as np

class SphereFn(BaseFunction):

    def __evaluate__(self, values):
        result = np.sum(np.power(values, 2))

        return result

class StyblinskiTangFn(BaseFunction):

    def __evaluate__(self, values):
        result = np.power(values, 4) - 16 * np.power(values,2) + 5 * values
        result = np.sum(result)

        return result

class HappyCatFn(BaseFunction):

    def __init__(self, inverted=False, alpha = 1/8):
        self.alpha = alpha
        super(HappyCatFn, self).__init__(inverted=inverted)

    def __evaluate__(self, values):
        norm = np.linalg.norm(values)
        result = np.power(norm, 2) - values.size
        result = np.power(np.power(result, 2), self.alpha)
        result = result + (1/values.size) * ( 0.5 * np.power(norm, 2) + np.sum(values))
        result = result + 0.5

        return result

class ShwefelFn(BaseFunction):
    """
    Schwefel 2.20 Function
    """
    def __evaluate__(self, values):
        result = np.abs(values)
        result = np.sum(result)

        return result

class QuarticFn(BaseFunction):

    def __init__(self, inverted=False):
        self._rnd = np.random.default_rng()
        super(QuarticFn, self).__init__(inverted=inverted)

    def __evaluate__(self, values):
        result = np.power(values, 4)
        result = result.flat * np.arange(0, result.size, step=1)
        result = result + self._rnd.random((result.size,))
        result = np.sum(result)

        return result

class HolderTableFn(BaseFunction):

    def __evaluate__(self, values):

        values = values.flatten()

        x = np.sum(values[:values.size//2])
        y = np.sum(values[values.size//2:])

        result = np.sqrt(np.power(x, 2) + np.power(y, 2))
        result = np.abs(1 - (result / np.pi))
        result = np.sin(x) * np.cos(y) * np.exp(result)
        result = -np.abs(result)
        result = max(result, -19.2085) - min(result, -19.2085)

        return result
