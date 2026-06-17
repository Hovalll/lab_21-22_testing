import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.leap_year import is_leap_year

class TestLeapYear(unittest.TestCase):
    
    def setUp(self):
        """Подготовка данных перед тестами"""
        self.leap_years = [2000, 2004, 2008, 2012, 2016, 2020, 2024, 2400]
        self.common_years = [2001, 2002, 2003, 2005, 2100, 1900, 1800]
    
    def test_leap_years(self):
        """Тест: високосные годы"""
        for year in self.leap_years:
            with self.subTest(year=year):
                self.assertTrue(is_leap_year(year))
    
    def test_common_years(self):
        """Тест: невисокосные годы"""
        for year in self.common_years:
            with self.subTest(year=year):
                self.assertFalse(is_leap_year(year))
    
    def test_century_years(self):
        """Тест: века (делятся на 100)"""
        self.assertTrue(is_leap_year(2000))   # делится на 400
        self.assertFalse(is_leap_year(1900))  # делится на 100, но не на 400
        self.assertFalse(is_leap_year(2100))  # делится на 100, но не на 400
    
    def test_invalid_years(self):
        """Тест: недопустимые годы"""
        for year in [0, -1, -100, -2024]:
            with self.subTest(year=year):
                self.assertFalse(is_leap_year(year))
    
    def test_non_integer_input(self):
        """Тест: нечисловые значения"""
        self.assertFalse(is_leap_year("2000"))
        self.assertFalse(is_leap_year(2000.5))
        self.assertFalse(is_leap_year(None))

if __name__ == '__main__':
    unittest.main()
