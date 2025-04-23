import pytest
from card_parts.name import Name
from card_parts.mana_cost import ManaCost, ManaSymbol
from game_objects.game_object import GameObject
from game_objects.card import Card
from game_objects.spell import Spell
from game_objects.permanent import (
    PermanentObject,
    PermanentCard,
    PermanentSpell,
    Permanent,
)
from players.player import Player
from status.status import Status, Tap, Flip, Facing, Phasing
from colors.color import Color


# Przykładowe dane do testów
@pytest.fixture
def example_name():
    return Name("Test Card", {"en": "Test Card"}, ["Test", "Card"])


@pytest.fixture
def example_mana_cost():
    mana_symbol = ManaSymbol("{R}")
    return ManaCost([mana_symbol])


@pytest.fixture
def example_player():
    return Player("Test Player")


@pytest.fixture
def example_permanent_object(example_name, example_mana_cost):
    return PermanentObject(
        example_name, example_mana_cost, "This is a test permanent object."
    )


@pytest.fixture
def example_permanent_card(example_name, example_mana_cost):
    return PermanentCard(
        example_name, example_mana_cost, "This is a test permanent card."
    )


@pytest.fixture
def example_permanent_spell(example_name, example_mana_cost, example_player):
    return PermanentSpell(
        example_player,
        example_player,
        example_name,
        example_mana_cost,
        "This is a test permanent spell.",
    )


@pytest.fixture
def example_permanent(example_name, example_mana_cost, example_player):
    return Permanent(
        example_player,
        example_player,
        example_name,
        example_mana_cost,
        "This is a test permanent.",
    )


# ---------- Testy dla PermanentObject ----------


def test_permanent_object_initialization(example_permanent_object):
    obj = example_permanent_object
    assert obj.name == example_permanent_object.name
    assert obj.mana_cost == example_permanent_object.mana_cost
    assert obj.colors == {Color.RED}


def test_permanent_object_get_characteristics(example_permanent_object):
    obj = example_permanent_object
    expected_characteristics = {
        "rules_text": "This is a test permanent object.",
        "name": obj.name,
        "mana cost": obj.mana_cost,
        "colors": [Color.RED.name],
    }
    assert obj.get_characteristics() == expected_characteristics


# ---------- Testy dla PermanentCard ----------


def test_permanent_card_inheritance(example_permanent_card):
    obj = example_permanent_card
    assert isinstance(obj, PermanentObject)
    assert isinstance(obj, Card)


# ---------- Testy dla PermanentSpell ----------


def test_permanent_spell_inheritance(example_permanent_spell):
    obj = example_permanent_spell
    assert isinstance(obj, PermanentObject)
    assert isinstance(obj, Spell)


def test_permanent_spell_owner_and_controller(example_permanent_spell, example_player):
    obj = example_permanent_spell
    assert obj._owner == example_player
    assert obj._controller == example_player


# ---------- Testy dla Permanent ----------


def test_permanent_initialization(example_permanent):
    obj = example_permanent
    assert obj.name == example_permanent.name
    assert obj.mana_cost == example_permanent.mana_cost
    assert obj.status.phasing == Phasing.PHASED_IN
    assert obj.colors == {Color.RED}


def test_permanent_tap(example_permanent):
    obj = example_permanent
    obj.tap()
    assert obj.status.tap == Tap.TAPPED


def test_permanent_untap(example_permanent):
    obj = example_permanent
    obj.untap()
    assert obj.status.tap == Tap.UNTAPPED


def test_permanent_flip(example_permanent):
    obj = example_permanent
    obj.flip()
    assert obj.status.flip == Flip.FLIPPED
    obj.flip()
    assert obj.status.flip == Flip.UNFLIPPED


def test_permanent_switch_facing(example_permanent):
    obj = example_permanent
    obj.switch_facing()
    assert obj.status.facing == Facing.FACE_DOWN
    obj.switch_facing()
    assert obj.status.facing == Facing.FACE_UP


def test_permanent_phase_out(example_permanent):
    obj = example_permanent
    obj.phase_out()
    assert obj.status.phasing == Phasing.PHASED_OUT


def test_permanent_phase_in(example_permanent):
    obj = example_permanent
    obj.phase_out()
    obj.phase_in()
    assert obj.status.phasing == Phasing.PHASED_IN
