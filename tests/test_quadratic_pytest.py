import pytest
from src.quadratic_solver import solve_quadratic

@pytest.mark.parametrize("a,b,c,expected_type,expected", [
    # Два корня
    (1, -5, 6, tuple, (3.0, 2.0)),
    (1, 0, -4, tuple, (2.0, -2.0)),
    # Один корень
    (1, -4, 4, tuple, (2.0,)),
    (1, 2, 1, tuple, (-1.0,)),
    # Нет корней
    (1, 0, 1, str, "Нет действительных корней"),
    # Линейное уравнение
    (0, 2, -4, tuple, (2.0,)),
    (0, 0, 0, str, "Бесконечное множество решений"),
])
def test_quadratic_parametrized(a, b, c, expected_type, expected):
    """Параметризованный тест квадратного уравнения"""
    result = solve_quadratic(a, b, c)
    assert isinstance(result, expected_type)
    if isinstance(result, tuple):
        assert len(result) == len(expected)
        for i in range(len(result)):
            assert abs(result[i] - expected[i]) < 0.000001
    else:
        assert result == expected
