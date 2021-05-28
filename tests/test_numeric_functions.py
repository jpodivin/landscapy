import unittest
import numpy as np
from landscapy import numeric_functions


class TestNumericFunction(unittest.TestCase):

    def setUp(self):

        self.test_values = np.ones((100,))
        super(TestNumericFunction, self).setUp()
