import pytest
from colors.color import Color


def test_from_symbol_valid():
    assert Color.from_symbol("W") == Color.WHITE
    assert Color.from_symbol("U") == Color.BLUE
    assert Color.from_symbol("B") == Color.BLACK
    assert Color.from_symbol("R") == Color.RED
    assert Color.from_symbol("G") == Color.GREEN


def test_from_symbol_valid_lowercase():
    assert Color.from_symbol("w") == Color.WHITE
    assert Color.from_symbol("u") == Color.BLUE


def test_from_symbol_invalid():
    with pytest.raises(ValueError, match="Unknown color letter: 'X'"):
        Color.from_symbol("X")

    with pytest.raises(ValueError, match="Unknown color letter: 'Z'"):
        Color.from_symbol("Z")
