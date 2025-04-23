from card_parts.name import Name
from colors.color import Color
from game_objects.game_object import GameObject
from game_objects.card import Card
from game_objects.spell import Spell
from players.player import Player
from status.status import Status, Tap, Flip, Facing, Phasing


class PermanentObject(GameObject):
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
        characteristics.update({"name": self._name, "color": self._color})
        return characteristics


class PermanentCard(PermanentObject, Card):
    pass


class PermanentSpell(PermanentObject, Spell):
    def __init__(
        self,
        owner: Player,
        controller: Player,
        name: Name,
        color: Color,
        rules_text: str,
    ):
        super().__init__(name=name, color=color, rules_text=rules_text)
        self._owner = owner
        self._controller = controller


class Permanent(PermanentObject):
    def __init__(
        self,
        owner: Player,
        controller: Player,
        name: Name,
        color: Color,
        rules_text: str,
    ):
        super().__init__(name=name, color=color, rules_text=rules_text)
        self._status = Status()
        self._owner = owner
        self._controller = controller

    @property
    def status(self) -> Status:
        return self._status

    def tap(self):
        self._status.tap = Tap.TAPPED

    def untap(self):
        self._status.tap = Tap.UNTAPPED

    def flip(self):
        if self._status.flip == Flip.UNFLIPPED:
            self._status.flip = Flip.FLIPPED
        else:
            self._status.flip = Flip.UNFLIPPED

    def switch_facing(self):
        if self._status.facing == Facing.FACE_UP:
            self._status.facing = Facing.FACE_DOWN
        else:
            self._status.facing = Facing.FACE_UP

    def phase_out(self):
        self._status.phasing = Phasing.PHASED_OUT

    def phase_in(self):
        self._status.phasing = Phasing.PHASED_IN
