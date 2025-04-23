import pytest
from game_objects.game_object import GameObject


# ---------- Testy dla klasy GameObject ----------


@pytest.fixture
def example_game_object():
    return GameObject("This is a test rule.")


def test_game_object_initialization(example_game_object):
    game_object = example_game_object

    # Sprawdzamy inicjalizację właściwości
    assert game_object.rules_text == "This is a test rule."
    assert game_object.owner is None
    assert game_object.controller is None


def test_get_characteristics(example_game_object):
    game_object = example_game_object
    expected_characteristics = {"rules_text": "This is a test rule."}

    # Sprawdzamy, czy metoda get_characteristics zwraca poprawne dane
    assert game_object.get_characteristics() == expected_characteristics


def test_owner_property(example_game_object):
    game_object = example_game_object
    # Sprawdzamy, czy property owner jest None na początku
    assert game_object.owner is None


def test_controller_property(example_game_object):
    game_object = example_game_object
    # Sprawdzamy, czy property controller jest None na początku
    assert game_object.controller is None
