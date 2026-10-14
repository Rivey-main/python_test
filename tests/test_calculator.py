# -*- coding: utf-8 -*-
import pytest

@pytest.mark.smoke
def test_add(calc):
    """Базовый тест операции сложения с использованием маркера smoke"""
    assert calc.add(2, 2) == 4

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (-1, 1, 0),
    (0, 0, 0),
    (10.5, 4.5, 15.0)
])
def test_add_parametrized(calc, a, b, expected):
    """Параметризованный тест для проверки различных комбинаций чисел"""
    assert calc.add(a, b) == expected

def test_divide_by_zero(calc):
    """Тест проверяет, что при делении на ноль генерируется ValueError"""
    with pytest.raises(ValueError) as exc_info:
        calc.divide(1, 0)
    assert str(exc_info.value) == "Деление на ноль"

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True)
])
def test_is_even(calc, number, expected):
    """Параметризованный тест для проверки четности чисел"""
    assert calc.is_even(number) == expected
