import numpy

class BaseFunction:

    def __call__(self, *values):
        
        return self.__evaluate__(values)

    def __evaluate__(self, *values):

        return 0.0