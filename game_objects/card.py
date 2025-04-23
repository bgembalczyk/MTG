from card_parts.name import Name
from colors.color import Color
from game_objects.game_object import GameObject


class Card(GameObject):
    """
    An object’s characteristics are name, mana cost, color, color indicator, card type, subtype, supertype, rules text,
    abilities, power, toughness, loyalty, defense, hand modifier, and life modifier.
    """

    def __init__(self, name: Name, color: Color, rules_text: str):
        super().__init__(rules_text=rules_text)
        self._name = name
        self._color = color

    @property
    def name(self) -> Name:
        return self._name

    @property
    def color(self) -> Color:
        return self._color

    def get_characteristics(self) -> dict:
        characteristics = super().get_characteristics()
        characteristics.update({"name": self.name, "color": self.color})
        return characteristics
