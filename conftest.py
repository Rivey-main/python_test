import pytest
from calculator import Calculator
from wheel_of_fortune import WheelOfFortune

@pytest.fixture
def calc():
    return Calculator()

@pytest.fixture
def game():
    return WheelOfFortune(word="автомобиль", max_errors=3)
