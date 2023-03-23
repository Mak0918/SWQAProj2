import unittest
from bmi_other import *


class TestBMICalculator(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(5, 10, 160), 22.9, delta=0.1)
        self.assertAlmostEqual(calculate_bmi(6, 0, 180), 24.4, delta=0.1)
        self.assertAlmostEqual(calculate_bmi(5, 4, 120), 20.6, delta=0.1)

    def test_get_bmi_category(self):
        self.assertEqual(get_bmi_category(16.0), UNDERWEIGHT)
        self.assertEqual(get_bmi_category(20.0), NORMAL_WEIGHT)
        self.assertEqual(get_bmi_category(26.0), OVERWEIGHT)
        self.assertEqual(get_bmi_category(35.0), OBESE)
