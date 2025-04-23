import pytest
from status.status import Status, Tap, Flip, Facing, Phasing

# ---------- Testy dla klasy Status ----------


@pytest.fixture
def status():
    return Status()


def test_initial_status(status):
    # Testowanie, czy początkowe wartości statusu są poprawne
    assert status.tap == Tap.UNTAPPED
    assert status.flip == Flip.UNFLIPPED
    assert status.facing == Facing.FACE_UP
    assert status.phasing == Phasing.PHASED_IN


def test_status_tap(status):
    # Testowanie zmiany tapu
    status.tap = Tap.TAPPED
    assert status.tap == Tap.TAPPED
    status.tap = Tap.UNTAPPED
    assert status.tap == Tap.UNTAPPED


def test_status_flip(status):
    # Testowanie zmiany flipu
    status.flip = Flip.FLIPPED
    assert status.flip == Flip.FLIPPED
    status.flip = Flip.UNFLIPPED
    assert status.flip == Flip.UNFLIPPED


def test_status_facing(status):
    # Testowanie zmiany facingu
    status.facing = Facing.FACE_DOWN
    assert status.facing == Facing.FACE_DOWN
    status.facing = Facing.FACE_UP
    assert status.facing == Facing.FACE_UP


def test_status_phasing(status):
    # Testowanie zmiany phasingu
    status.phasing = Phasing.PHASED_OUT
    assert status.phasing == Phasing.PHASED_OUT
    status.phasing = Phasing.PHASED_IN
    assert status.phasing == Phasing.PHASED_IN
