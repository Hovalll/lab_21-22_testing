import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.sorter import sort_descending, is_sorted_descending

class TestSortDescending(unittest.TestCase):
    
    def test_sort_integers(self):
        """Тест: сортировка целых чисел"""
        arr = [5, 2, 8, 1, 9, 3]
        sorted_arr = sort_descending(arr)
        self.assertEqual(sorted_arr, [9, 8, 5, 3, 2, 1])
        self.assertTrue(is_sorted_descending(sorted_arr))
        # Проверяем, что исходный список не изменился
        self.assertEqual(arr, [5, 2, 8, 1, 9, 3])
    
    def test_sort_floats(self):
        """Тест: сортировка чисел с плавающей точкой"""
        arr = [3.14, 2.71, 1.41, 0.58]
        sorted_arr = sort_descending(arr)
        self.assertEqual(sorted_arr, [3.14, 2.71, 1.41, 0.58])
        self.assertTrue(is_sorted_descending(sorted_arr))
    
    def test_sort_negative_numbers(self):
        """Тест: сортировка отрицательных чисел"""
        arr = [-5, -2, -8, -1, -9]
        sorted_arr = sort_descending(arr)
        self.assertEqual(sorted_arr, [-1, -2, -5, -8, -9])
        self.assertTrue(is_sorted_descending(sorted_arr))
    
    def test_empty_list(self):
        """Тест: пустой список"""
        sorted_arr = sort_descending([])
        self.assertEqual(sorted_arr, [])
        self.assertTrue(is_sorted_descending(sorted_arr))
    
    def test_single_element(self):
        """Тест: список с одним элементом"""
        sorted_arr = sort_descending([42])
        self.assertEqual(sorted_arr, [42])
        self.assertTrue(is_sorted_descending(sorted_arr))
    
    def test_duplicates(self):
        """Тест: список с дубликатами"""
        arr = [5, 2, 5, 1, 5, 3]
        sorted_arr = sort_descending(arr)
        self.assertEqual(sorted_arr, [5, 5, 5, 3, 2, 1])
        self.assertTrue(is_sorted_descending(sorted_arr))
    
    def test_already_sorted(self):
        """Тест: уже отсортированный список"""
        arr = [9, 7, 5, 3, 1]
        sorted_arr = sort_descending(arr)
        self.assertEqual(sorted_arr, [9, 7, 5, 3, 1])
        self.assertTrue(is_sorted_descending(sorted_arr))
    
    def test_invalid_input(self):
        """Тест: недопустимые входные данные"""
        with self.assertRaises(TypeError):
            sort_descending("not a list")
        
        with self.assertRaises(TypeError):
            sort_descending(123)
    
    def test_mixed_types(self):
        """Тест: смешанные типы данных"""
        with self.assertRaises(TypeError):
            sort_descending([1, "two", 3])

if __name__ == '__main__':
    unittest.main()
