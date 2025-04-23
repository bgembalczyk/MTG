import pytest
from card_parts.name import Name


# ---------- Testy dla klasy Name ----------


def test_name_initialization():
    # Tworzymy instancję klasy Name
    name = Name("Alice", {"en": "Alice", "pl": "Alicja"}, ["Al", "Ali"])

    # Sprawdzamy, czy właściwości zostały poprawnie zainicjowane
    assert name.name == "Alice"
    assert name.names_in_language == {"en": "Alice", "pl": "Alicja"}
    assert name.other_names == ["Al", "Ali"]


def test_str_method():
    name = Name("Alice", {"en": "Alice", "pl": "Alicja"}, ["Al", "Ali"])
    # Sprawdzamy, czy metoda __str__ zwraca poprawną nazwę
    assert str(name) == "Alice"


def test_all_names():
    name = Name("Alice", {"en": "Alice", "pl": "Alicja"}, ["Al", "Ali"])
    # Sprawdzamy, czy all_names łączy główną nazwę i inne nazwy
    assert name.all_names == ["Alice", "Al", "Ali"]


def test_names_in_language():
    name = Name("Alice", {"en": "Alice", "pl": "Alicja"}, ["Al", "Ali"])
    # Sprawdzamy, czy zwracana jest poprawna mapa nazw w językach
    assert name.names_in_language == {"en": "Alice", "pl": "Alicja"}


def test_other_names():
    name = Name("Alice", {"en": "Alice", "pl": "Alicja"}, ["Al", "Ali"])
    # Sprawdzamy, czy lista innych nazw jest poprawna
    assert name.other_names == ["Al", "Ali"]


def test_all_names_empty_other_names():
    name = Name("Alice", {"en": "Alice", "pl": "Alicja"}, [])
    # Sprawdzamy, czy all_names zwraca tylko główną nazwę, gdy inne są puste
    assert name.all_names == ["Alice"]


def test_names_in_language_empty():
    name = Name("Alice", {}, ["Al", "Ali"])
    # Sprawdzamy, czy names_in_language zwraca pusty słownik, gdy brak nazw w innych językach
    assert name.names_in_language == {}
