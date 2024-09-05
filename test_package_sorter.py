# File: test_package_sorter.py

import unittest
from package_sorter import sort

class TestPackageSorting(unittest.TestCase):
    def test_standard_package(self):
        self.assertEqual(sort(100, 100, 99, 19.99), "STANDARD")
        
    def test_bulky_package(self):
        self.assertEqual(sort(150, 50, 50, 15), "SPECIAL")
        
    def test_heavy_package(self):
        self.assertEqual(sort(99, 99, 99, 20), "SPECIAL")
        
    def test_rejected_package(self):
        self.assertEqual(sort(150, 150, 150, 25), "REJECTED")
        
    def test_edge_case_volume(self):
        self.assertEqual(sort(100, 100, 100, 15), "SPECIAL")
        self.assertEqual(sort(100, 100, 100.01, 15), "SPECIAL")
        
    def test_edge_case_dimension(self):
        self.assertEqual(sort(149.99, 50, 50, 15), "STANDARD")
        self.assertEqual(sort(150, 50, 50, 15), "SPECIAL")
        
    def test_edge_case_mass(self):
        self.assertEqual(sort(99, 99, 99, 19.99), "STANDARD")
        self.assertEqual(sort(99, 99, 99, 20), "SPECIAL")
        
    def test_zero_inputs(self):
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")
        
    def test_float_inputs(self):
        self.assertEqual(sort(149.99, 149.99, 149.99, 19.99), "SPECIAL")
        self.assertEqual(sort(150.01, 150.01, 150.01, 20.01), "REJECTED")
        
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            sort(-1, 100, 100, 10)
        with self.assertRaises(ValueError):
            sort(100, "not a number", 100, 10)

if __name__ == "__main__":
    unittest.main()