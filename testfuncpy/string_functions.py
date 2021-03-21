import string
import numpy as np
from testfuncpy.base_function import BaseFunction

class CharInclusionFn(BaseFunction):

    def __init__(self, inverted=False, target_set=string.ascii_lowercase):
        self.target_set = target_set
        super(CharInclusionFn, self).__init__(inverted=inverted)

    def __evaluate__(self, individual):
        result = 0
        for index in range(individual.size):
            if individual[index] in self.target_set:
                result += 1

        return result/individual.size
