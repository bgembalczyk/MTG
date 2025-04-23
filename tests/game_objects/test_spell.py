import pytest
from game_objects.spell import Spell
from game_objects.game_object import GameObject
from players.player import Player


# Przykładowe dane do testów
@pytest.fixture
def example_player():
    return Player("Test Player")


@pytest.fixture
def example_spell(example_player):
    return Spell(example_player, example_player, "This is a test spell.")


# ---------- Testy dla klasy Spell ----------


def test_spell_initialization(example_spell, example_player):
    spell = example_spell
    # Testowanie, czy właściwości zostały poprawnie przypisane
    assert spell.rules_text == "This is a test spell."
    assert spell._owner == example_player
    assert spell._controller == example_player


def test_spell_inheritance(example_spell):
    spell = example_spell
    # Testowanie, czy Spell dziedziczy po GameObject
    assert isinstance(spell, GameObject)


def test_spell_owner(example_spell, example_player):
    spell = example_spell
    # Testowanie, czy właściciel jest poprawnie przypisany
    assert spell._owner == example_player


def test_spell_controller(example_spell, example_player):
    spell = example_spell
    # Testowanie, czy kontroler jest poprawnie przypisany
    assert spell._controller == example_player


def test_spell_get_characteristics(example_spell):
    spell = example_spell
    # Testowanie, czy można uzyskać charakterystyki
    expected_characteristics = {"rules_text": spell.rules_text}
    assert spell.get_characteristics() == expected_characteristics
