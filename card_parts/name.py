class Name:
    def __init__(self, name: str, names_in_language: dict, other_names: list):
        self._name = name
        self._names_in_language = names_in_language
        self._other_names = other_names

    def __str__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        return self._name

    @property
    def names_in_language(self) -> dict:
        return self._names_in_language

    @property
    def other_names(self) -> list:
        return self._other_names

    @property
    def all_names(self) -> list:
        return [self._name] + self._other_names
