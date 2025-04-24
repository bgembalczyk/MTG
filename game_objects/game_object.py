class GameObject:
    """
    An object’s characteristics are name, mana cost, color, color indicator, card type, subtype, supertype, rules text,
    abilities, power, toughness, loyalty, defense, hand modifier, and life modifier.
    """

    def __init__(self, rules_text: str, *args, **kwargs):
        self._owner = None
        self._controller = None
        self._rules_text = rules_text

    @property
    def owner(self):
        return self._owner

    @property
    def controller(self):
        return self._controller

    @property
    def rules_text(self) -> str:
        return self._rules_text

    def get_characteristics(self) -> dict:
        """
        Returns a dictionary of the object's characteristics.
        """
        return {"rules_text": self.rules_text}
