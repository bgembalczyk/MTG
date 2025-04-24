from card_parts.mana_cost import ManaCost
from card_parts.name import Name
from colors.color import Color
from game_objects.game_object import GameObject
from game_objects.card import Card
from game_objects.spell import Spell
from players.player import Player
from status.status import Status, Tap, Flip, Facing, Phasing


class PermanentMixin:
    """
    Mixin dodający właściwości stałych obiektów: name, mana_cost, colors.
    """

    def __init__(self, name: Name, mana_cost: ManaCost, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Pass all args/kwargs to super()
        self._name = name
        self._mana_cost = mana_cost

    @property
    def name(self) -> Name:
        return self._name

    @property
    def mana_cost(self) -> ManaCost:
        return self._mana_cost

    @property
    def colors(self) -> set:
        return self.mana_cost.colors if self.mana_cost else set()

    def get_characteristics(self) -> dict:
        base = {}
        if hasattr(super(), "get_characteristics"):
            base = super().get_characteristics()
        base.update(
            {
                "name": self.name,
                "mana cost": self.mana_cost,
                "colors": self.colors,
            }
        )
        return base


class PermanentCard(PermanentMixin, Card):
    def __init__(
        self, name: Name, mana_cost: ManaCost, rules_text: str, *args, **kwargs
    ):
        super().__init__(
            name=name, mana_cost=mana_cost, rules_text=rules_text, *args, **kwargs
        )


class PermanentSpell(PermanentMixin, Spell):
    def __init__(
        self,
        owner: Player,
        controller: Player,
        name: Name,
        mana_cost: ManaCost,
        rules_text: str,
        *args,
        **kwargs,
    ):
        # Wywołanie konstruktora Spell z odpowiednimi argumentami
        super().__init__(
            name=name,
            owner=owner,
            controller=controller,
            mana_cost=mana_cost,
            rules_text=rules_text,
            *args,
            **kwargs,
        )
        self._owner = owner
        self._controller = controller


class Permanent(PermanentMixin, GameObject):
    def __init__(
        self,
        owner: Player,
        controller: Player,
        name: Name,
        mana_cost: ManaCost,
        rules_text: str,
        *args,
        **kwargs,
    ):
        self._status = Status()
        self._owner = owner
        self._controller = controller
        super().__init__(
            name=name, mana_cost=mana_cost, rules_text=rules_text, *args, **kwargs
        )

    @property
    def status(self) -> Status:
        return self._status

    def tap(self):
        self._status.tap = Tap.TAPPED

    def untap(self):
        self._status.tap = Tap.UNTAPPED

    def flip(self):
        self._status.flip = (
            Flip.FLIPPED if self._status.flip == Flip.UNFLIPPED else Flip.UNFLIPPED
        )

    def switch_facing(self):
        self._status.facing = (
            Facing.FACE_DOWN
            if self._status.facing == Facing.FACE_UP
            else Facing.FACE_UP
        )

    def phase_out(self):
        self._status.phasing = Phasing.PHASED_OUT

    def phase_in(self):
        self._status.phasing = Phasing.PHASED_IN
