import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.leap_year import is_leap_year

@pytest.fixture
def leap_years():
    return [2000, 2004, 2008, 2012, 2016, 2020, 2024, 2400]

@pytest.fixture
def common_years():
    return [2001, 2002, 2003, 2005, 2100, 1900, 1800, 2023, 2025]

def test_leap_years(leap_years):
    for year in leap_years:
        assert is_leap_year(year) is True

def test_common_years(common_years):
    for year in common_years:
        assert is_leap_year(year) is False

@pytest.mark.parametrize("year,expected", [
    (2000, True),
    (2001, False),
    (2004, True),
    (2100, False),
    (2400, True),
])
def test_leap_year_parametrized(year, expected):
    assert is_leap_year(year) == expected

@pytest.mark.parametrize("year", [0, -1, -100, -2024])
def test_invalid_years(year):
    assert is_leap_year(year) is False

@pytest.mark.parametrize("input_value", ["2000", 2000.5, None])
def test_non_integer_input(input_value):
    assert is_leap_year(input_value) is False
