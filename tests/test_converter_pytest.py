import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.converter import convert_to_int

@pytest.mark.parametrize("input_str,expected", [
    ("123", 123),
    ("-123", -123),
    ("+42", 42),
    ("0", 0),
    ("-0", 0),
    ("00042", 42),
    ("  -42  ", -42),
    ("  123  ", 123),
])
def test_valid_conversions(input_str, expected):
    """Тест: валидные конвертации"""
    success, value, message = convert_to_int(input_str)
    assert success is True
    assert value == expected
    assert message == "Успешно"

@pytest.mark.parametrize("input_str,expected_error", [
    ("", "Ошибка: пустая строка"),
    ("   ", "Ошибка: строка состоит только из пробелов"),
    ("12a3", "Ошибка: недопустимый символ 'a'"),
    ("12.3", "Ошибка: недопустимый символ '.'"),
    ("-", "Ошибка: после знака отсутствуют цифры"),
    ("+", "Ошибка: после знака отсутствуют цифры"),
    ("abc", "Ошибка: недопустимый символ 'a'"),
])
def test_invalid_conversions(input_str, expected_error):
    """Тест: невалидные конвертации"""
    success, value, message = convert_to_int(input_str)
    assert success is False
    assert value is None
    assert message == expected_error

def test_non_string_input():
    """Тест: входное значение не строка"""
    success, value, message = convert_to_int(123)
    assert success is False
    assert value is None
    assert message == "Ошибка: входное значение должно быть строкой"
