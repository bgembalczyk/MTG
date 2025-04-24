from card_parts.mana_cost import ManaCost
from card_parts.name import Name
from colors.color import Color
from game_objects.game_object import GameObject


class Card(GameObject):
    def __init__(self, name: Name, mana_cost: ManaCost, rules_text: str, *args, **kwargs):
        self._name = name
        self._mana_cost = mana_cost
        super().__init__(rules_text=rules_text, *args, **kwargs)

    @property
    def name(self) -> Name:
        return self._name

    @property
    def mana_cost(self) -> ManaCost:
        return self._mana_cost

    @property
    def colors(self) -> set:
        return self.mana_cost.colors

    def get_characteristics(self) -> dict:
        characteristics = super().get_characteristics()
        characteristics.update(
            {
                "name": self.name,
                "mana cost": self.mana_cost,
                "colors": sorted(self.colors),
            }
        )
        return characteristics
