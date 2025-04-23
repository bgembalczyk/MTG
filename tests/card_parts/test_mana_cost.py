import pytest
from card_parts.mana_cost import ManaCost, ManaSymbol
from colors.color import Color

# ---------- ManaSymbol ----------


def test_valid_symbols():
    valid = [
        "{W}",
        "{U}",
        "{B}",
        "{R}",
        "{G}",
        "{C}",
        "{X}",
        "{1}",
        "{10}",
        "{W/U}",
        "{2/B}",
        "{G/U/P}",
    ]
    for s in valid:
        ms = ManaSymbol(s)
        assert ms.symbol == s


def test_invalid_symbols():
    invalid = ["X", "{Z}", "{/G}", "{W//U}", "{}"]
    for s in invalid:
        with pytest.raises(ValueError):
            ManaSymbol(s)


def test_split():
    assert ManaSymbol("{W/U}").split() == ["W", "U"]
    assert ManaSymbol("{2/B}").split() == ["2", "B"]
    assert ManaSymbol("{G/U/P}").split() == ["G", "U", "P"]


def test_mana_value():
    assert ManaSymbol("{W}").mana_value == 1
    assert ManaSymbol("{2/B}").mana_value == 2  # 2 + 1
    assert ManaSymbol("{X}").mana_value == 0
    assert ManaSymbol("{1}").mana_value == 1
    assert ManaSymbol("{5}").mana_value == 5
    assert ManaSymbol("{W/U/P}").mana_value == 1


def test_color_extraction():
    assert Color.WHITE in ManaSymbol("{W}").colors
    assert Color.BLUE in ManaSymbol("{U}").colors
    assert Color.BLACK in ManaSymbol("{B/R}").colors
    assert Color.RED in ManaSymbol("{B/R}").colors
    assert Color.GREEN in ManaSymbol("{G/U/P}").colors
    assert Color.BLUE in ManaSymbol("{G/U/P}").colors


# ---------- ManaCost ----------


def test_mana_cost_value():
    cost = ManaCost([ManaSymbol("{W}"), ManaSymbol("{1}"), ManaSymbol("{2/B}")])
    assert cost.mana_value == 1 + 1 + 2


def test_mana_cost_colors():
    cost = ManaCost(
        [
            ManaSymbol("{W}"),
            ManaSymbol("{B/R}"),
            ManaSymbol("{X}"),
        ]
    )
    colors = cost.colors
    assert Color.WHITE in colors
    assert Color.BLACK in colors
    assert Color.RED in colors
