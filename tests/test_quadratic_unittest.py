import unittest
import sys
import os

# Добавляем корневую папку в путь
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.quadratic_solver import solve_quadratic

class TestQuadraticSolver(unittest.TestCase):
    
    def setUp(self):
        """Подготовка данных перед каждым тестом"""
        self.epsilon = 0.000001
    
    def test_two_roots(self):
        """Тест: два корня (дискриминант > 0)"""
        result = solve_quadratic(1, -5, 6)
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], 3.0, delta=self.epsilon)
        self.assertAlmostEqual(result[1], 2.0, delta=self.epsilon)
    
    def test_one_root(self):
        """Тест: один корень (дискриминант = 0)"""
        result = solve_quadratic(1, -4, 4)
        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0], 2.0, delta=self.epsilon)
    
    def test_no_roots(self):
        """Тест: нет корней (дискриминант < 0)"""
        result = solve_quadratic(1, 0, 1)
        self.assertEqual(result, "Нет действительных корней")
    
    def test_linear_equation(self):
        """Тест: линейное уравнение (a = 0)"""
        result = solve_quadratic(0, 2, -4)
        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0], 2.0, delta=self.epsilon)
    
    def test_identity_equation(self):
        """Тест: тождество (все числа - решения)"""
        result = solve_quadratic(0, 0, 0)
        self.assertEqual(result, "Бесконечное множество решений")

if __name__ == '__main__':
    unittest.main()
