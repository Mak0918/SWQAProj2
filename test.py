import unittest
from bmi_calculator import *

class TestBMICalculator(unittest.TestCase):
    
    def test_underweight(self):
        # Test cases for underweight category
        self.assertEqual(calculate_bmi(100, 5, 2), 18.2) # borderline case
        self.assertEqual(calculate_bmi(110, 5, 2), 20.1)
        self.assertEqual(calculate_bmi(120, 5, 5), 19.9)
        self.assertEqual(calculate_bmi(90, 5, 0), 17.7)
        self.assertEqual(calculate_bmi(95, 4, 11), 19.2)

    def test_normal_weight(self):
        # Test cases for normal weight category
        self.assertEqual(calculate_bmi(140, 5, 6), 22.6) # borderline case
        self.assertEqual(calculate_bmi(150, 5, 5), 24.9) 
        self.assertEqual(calculate_bmi(155, 5, 9), 22.8)
        self.assertEqual(calculate_bmi(165, 5, 8), 25.0)
        self.assertEqual(calculate_bmi(175, 5, 7), 27.3)
    
    def test_overweight(self):
        # Test cases for overweight category
        self.assertEqual(calculate_bmi(200, 6, 0), 27.2) # borderline case
        self.assertEqual(calculate_bmi(180, 5, 10), 25.8)
        self.assertEqual(calculate_bmi(195, 5, 9), 28.8)
        self.assertEqual(calculate_bmi(190, 5, 6), 30.8)
        self.assertEqual(calculate_bmi(185, 5, 4), 31.7)
        
    def test_obese(self):
        # Test cases for obese category
        self.assertEqual(calculate_bmi(220, 6, 1), 29.1) # borderline case
        self.assertEqual(calculate_bmi(230, 5, 11), 32.0)
        self.assertEqual(calculate_bmi(240, 5, 9), 35.4)
        self.assertEqual(calculate_bmi(250, 5, 7), 39.1)
        self.assertEqual(calculate_bmi(260, 5, 5), 43.0)
        
if __name__ == '__main__':
    unittest.main()