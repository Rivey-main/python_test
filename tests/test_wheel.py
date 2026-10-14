import pytest
from wheel_of_fortune import WheelOfFortune

@pytest.mark.smoke
def test_initial_display_word(game):
    assert game.get_display_word() == "**********"

def test_correct_guess(game):
    assert game.guess_letter("а") is True
    assert game.get_display_word() == "а*********"

def test_wrong_guess(game):
    assert game.guess_letter("х") is False
    assert game.errors == 1

def test_invalid_input(game):
    with pytest.raises(ValueError):
        game.guess_letter("1")
    with pytest.raises(ValueError):
        game.guess_letter("многобукв")

def test_game_win(game):
    for letter in "автомобиль":
        game.guess_letter(letter)
    assert game.is_won() is True

def test_game_loss(game):
    game.guess_letter("х")
    game.guess_letter("й")
    game.guess_letter("з")
    assert game.is_game_over() is True
