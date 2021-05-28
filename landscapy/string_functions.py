import string
import numpy as np
from landscapy.base_functions import BaseFunction

class CharInclusionFn(BaseFunction):
    """
    """
    def __init__(self, inverted=False, target_set=string.ascii_lowercase):
        self.target_set = target_set
        super(CharInclusionFn, self).__init__(inverted=inverted)

    def __evaluate__(self, string):
        result = 0
        for index in range(string.size):
            if string[index] in self.target_set:
                result += 1

        return result/string.size
