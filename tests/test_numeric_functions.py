import unittest
import numpy as np
from landscapy import numeric_functions as nf


class TestNumericFunction(unittest.TestCase):

    def setUp(self):

        self.test_values = np.ones((100,))
        super(TestNumericFunction, self).setUp()

    def test_holder_table_fn(self):

        function = nf.HolderTableFn()

        result = function(self.test_values)
