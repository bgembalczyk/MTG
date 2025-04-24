from game_objects.game_object import GameObject
from players.player import Player


class Spell(GameObject):
    def __init__(
        self, owner: Player, controller: Player, rules_text: str, *args, **kwargs
    ):
        super().__init__(rules_text=rules_text, *args, **kwargs)
        self._owner = owner
        self._controller = controller
