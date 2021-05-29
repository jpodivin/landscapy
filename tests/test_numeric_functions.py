import unittest
import numpy as np
from landscapy import numeric_functions as nf


class TestNumericFunction(unittest.TestCase):

    def setUp(self):

        self.test_values = np.ones((10,))
        super(TestNumericFunction, self).setUp()

    def test_holder_table_fn(self):

        function = nf.HolderTableFn()

        result = function(self.test_values)

        self.assertEqual(function.evaluated, 1)
        self.assertAlmostEqual(result, -0.95016120789)
        self.assertFalse(function.optimum_reached(self.test_values))
