import unittest
import sys
import os

# Добавляем корневую папку в путь
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.converter import convert_to_int

class TestStringToIntConverter(unittest.TestCase):
    
    def test_valid_positive_numbers(self):
        """Тест: корректные положительные числа"""
        success, value, message = convert_to_int("123")
        self.assertTrue(success)
        self.assertEqual(value, 123)
        self.assertEqual(message, "Успешно")
        
        success, value, message = convert_to_int("0")
        self.assertTrue(success)
        self.assertEqual(value, 0)
        
        success, value, message = convert_to_int("00042")
        self.assertTrue(success)
        self.assertEqual(value, 42)
    
    def test_valid_negative_numbers(self):
        """Тест: корректные отрицательные числа"""
        success, value, message = convert_to_int("-123")
        self.assertTrue(success)
        self.assertEqual(value, -123)
        
        success, value, message = convert_to_int("-0")
        self.assertTrue(success)
        self.assertEqual(value, 0)
    
    def test_valid_with_plus_sign(self):
        """Тест: числа со знаком +"""
        success, value, message = convert_to_int("+42")
        self.assertTrue(success)
        self.assertEqual(value, 42)
    
    def test_with_whitespace(self):
        """Тест: строки с пробелами"""
        success, value, message = convert_to_int("  123  ")
        self.assertTrue(success)
        self.assertEqual(value, 123)
        
        success, value, message = convert_to_int("  -42  ")
        self.assertTrue(success)
        self.assertEqual(value, -42)
    
    def test_empty_string(self):
        """Тест: пустая строка"""
        success, value, message = convert_to_int("")
        self.assertFalse(success)
        self.assertIsNone(value)
        self.assertEqual(message, "Ошибка: пустая строка")
    
    def test_only_spaces(self):
        """Тест: строка из пробелов"""
        success, value, message = convert_to_int("   ")
        self.assertFalse(success)
        self.assertIsNone(value)
        self.assertEqual(message, "Ошибка: строка состоит только из пробелов")
    
    def test_invalid_characters(self):
        """Тест: недопустимые символы"""
        success, value, message = convert_to_int("12a3")
        self.assertFalse(success)
        self.assertIsNone(value)
        self.assertEqual(message, "Ошибка: недопустимый символ 'a'")
        
        success, value, message = convert_to_int("12.3")
        self.assertFalse(success)
        self.assertIsNone(value)
        self.assertEqual(message, "Ошибка: недопустимый символ '.'")
    
    def test_just_sign(self):
        """Тест: только знак без цифр"""
        success, value, message = convert_to_int("-")
        self.assertFalse(success)
        self.assertIsNone(value)
        self.assertEqual(message, "Ошибка: после знака отсутствуют цифры")
        
        success, value, message = convert_to_int("+")
        self.assertFalse(success)
        self.assertIsNone(value)
        self.assertEqual(message, "Ошибка: после знака отсутствуют цифры")
    
    def test_non_string_input(self):
        """Тест: входное значение не строка"""
        success, value, message = convert_to_int(123)
        self.assertFalse(success)
        self.assertIsNone(value)
        self.assertEqual(message, "Ошибка: входное значение должно быть строкой")

if __name__ == '__main__':
    unittest.main()

