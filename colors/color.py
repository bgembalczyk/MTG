from enum import Enum


class Color(Enum):
    WHITE = "white"
    BLUE = "blue"
    BLACK = "black"
    RED = "red"
    GREEN = "green"

    def __str__(self):
        return self.name

    @classmethod
    def from_symbol(cls, symbol: str):
        mapping = {
            "W": cls.WHITE,
            "U": cls.BLUE,  # "U" = Blue w MTG
            "B": cls.BLACK,
            "R": cls.RED,
            "G": cls.GREEN,
        }
        try:
            return mapping[symbol.upper()]
        except KeyError:
            raise ValueError(f"Unknown color letter: '{symbol}'")
