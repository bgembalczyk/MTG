import pytest
from card_parts.name import Name
from card_parts.mana_cost import ManaCost, ManaSymbol
from game_objects.game_object import GameObject
from colors.color import Color
from game_objects.card import Card


# Przykładowe dane do testów
@pytest.fixture
def example_name():
    return Name("Fireball", {"en": "Fireball"}, ["Flame", "Fire"])


@pytest.fixture
def example_mana_cost():
    mana_symbol_1 = ManaSymbol("{R}")
    mana_symbol_2 = ManaSymbol("{1}")
    return ManaCost([mana_symbol_1, mana_symbol_2])


@pytest.fixture
def example_card(example_name, example_mana_cost):
    return Card(example_name, example_mana_cost, "Deal 4 damage to any target.")


# ---------- Testy dla klasy Card ----------


def test_card_initialization(example_name, example_mana_cost):
    card = Card(example_name, example_mana_cost, "Deal 4 damage to any target.")

    # Sprawdzamy inicjalizację właściwości
    assert card.name == example_name
    assert card.mana_cost == example_mana_cost
    assert card.colors == {Color.RED}


def test_card_colors(example_card):
    card = example_card
    # Sprawdzamy, czy kolor karty jest poprawny
    assert card.colors == {Color.RED}


def test_get_characteristics(example_card):
    card = example_card
    expected_characteristics = {
        "name": example_card.name,
        "mana cost": example_card.mana_cost,
        "colors": {Color.RED},
        "rules_text": example_card.rules_text,
    }
    # Sprawdzamy, czy metoda get_characteristics zwraca poprawne dane
    assert card.get_characteristics() == expected_characteristics


def test_card_inheritance(example_card):
    card = example_card
    # Sprawdzamy, czy klasa Card dziedziczy po GameObject
    assert isinstance(card, GameObject)
