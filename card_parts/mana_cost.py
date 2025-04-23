import re

from colors.color import Color


class ManaSymbol:
    def __init__(self, symbol: str):
        self._symbol = symbol
        pattern = r"\{(?:[WUBRGCXS]|\d+)(?:\/[WUBRGCP])*\}"
        mana_symbol_regex = re.compile(pattern)
        if not mana_symbol_regex.fullmatch(self.symbol):
            raise ValueError(f"Invalid mana symbol: {self.symbol}")

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def mana_value(self) -> int:
        symbols = self.split()
        mana_value = 0
        for symbol in symbols:
            try:
                mana_value += int(symbol)
            except ValueError:
                if symbol is not "X":
                    mana_value += 1
        return mana_value

    @property
    def color(self) -> set:
        """
        Returns the color of the mana symbol.
        """
        colors = set()
        for symbol in self.split():
            try:
                colors.update(Color.from_symbol(symbol))
            except ValueError:
                continue
        return colors

    def split(self) -> list:
        """
        Splits the mana symbol into its components.
        """
        return [self._symbol[i : i + 2] for i in range(1, len(self._symbol) - 1, 2)]


class ManaCost:
    def __init__(self, list_of_mana_symbols: list):
        self._list_of_mana_symbols = list_of_mana_symbols

    @property
    def list_of_mana_symbols(self) -> list:
        return self._list_of_mana_symbols

    @property
    def mana_value(self) -> int:
        """
        Returns the total mana value of the mana cost.
        """
        return sum(symbol.mana_value for symbol in self.list_of_mana_symbols)

    @property
    def colors(self) -> set:
        """
        Returns the colors of the mana cost.
        """
        colors = set()
        for symbol in self.list_of_mana_symbols:
            colors.add(symbol.color)
        return colors
