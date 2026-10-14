import pytest
from wheel_of_fortune import WheelOfFortune

@pytest.fixture
def game():
    return WheelOfFortune(word="автомобиль", max_errors=3)
