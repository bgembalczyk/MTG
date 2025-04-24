# test_permanent.py
import pytest
from game_objects.permanent import (
    PermanentMixin,
    PermanentCard,
    PermanentSpell,
    Permanent,
)
from card_parts.name import Name
from card_parts.mana_cost import ManaCost, ManaSymbol
from players.player import Player
from status.status import Tap, Flip, Facing, Phasing


@pytest.fixture
def example_name():
    return Name(name="<NAME>", names_in_language={}, other_names=[])


@pytest.fixture
def example_mana_cost():
    return ManaCost([ManaSymbol("{1}"), ManaSymbol("{W}"), ManaSymbol("{U}")])


@pytest.fixture
def example_rules_text():
    return "This is a test permanent object."


@pytest.fixture
def player():
    return Player("Player 1")


@pytest.fixture
def opponent():
    return Player("Player 2")


def test_permanent_card_characteristics(
    example_name, example_mana_cost, example_rules_text
):
    card = PermanentCard(
        name=example_name, mana_cost=example_mana_cost, rules_text=example_rules_text
    )
    characteristics = card.get_characteristics()

    assert characteristics["name"] == example_name
    assert characteristics["mana cost"] == example_mana_cost
    assert characteristics["colors"] == example_mana_cost.colors
    assert characteristics["rules_text"] == example_rules_text


def test_permanent_spell_characteristics(
    example_name, example_mana_cost, example_rules_text, player, opponent
):
    spell = PermanentSpell(
        player, opponent, example_name, example_mana_cost, example_rules_text
    )
    characteristics = spell.get_characteristics()

    assert characteristics["name"] == example_name
    assert characteristics["mana cost"] == example_mana_cost
    assert example_mana_cost.colors == characteristics["colors"]
    assert characteristics["rules_text"] == example_rules_text
    assert spell.owner == player
    assert spell.controller == opponent


def test_permanent_status_transitions(
    example_name, example_mana_cost, example_rules_text, player, opponent
):
    permanent = Permanent(
        player, opponent, example_name, example_mana_cost, example_rules_text
    )

    # Tap and untap
    permanent.tap()
    assert permanent.status.tap == Tap.TAPPED
    permanent.untap()
    assert permanent.status.tap == Tap.UNTAPPED

    # Flip
    permanent.flip()
    assert permanent.status.flip == Flip.FLIPPED
    permanent.flip()
    assert permanent.status.flip == Flip.UNFLIPPED

    # Switch facing
    permanent.switch_facing()
    assert permanent.status.facing == Facing.FACE_DOWN
    permanent.switch_facing()
    assert permanent.status.facing == Facing.FACE_UP

    # Phase out/in
    permanent.phase_out()
    assert permanent.status.phasing == Phasing.PHASED_OUT
    permanent.phase_in()
    assert permanent.status.phasing == Phasing.PHASED_IN
