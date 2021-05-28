import unittest
import numpy as np
from landscapy import base_functions


class TestBaseFunction(unittest.TestCase):

    def setUp(self):

        self.test_values = np.ones((100,))
        super(TestBaseFunction, self).setUp()

    def test_function_init(self):

        test_function = base_functions.BaseFunction()

        self.assertFalse(test_function.inverted)

    def test_function_init_inverted(self):

        test_function = base_functions.BaseFunction(inverted=True)

        self.assertTrue(test_function.inverted)

    def test_evaluate(self):

        test_function = base_functions.BaseFunction()

        self.assertEqual(test_function(self.test_values), 0.0)

    def test_evaluate_inverted(self):

        test_function = base_functions.BaseFunction(True)

        self.assertEqual(test_function(self.test_values), 1.0)
