from enum import Enum


class Tap(Enum):
    UNTAPPED = 0
    TAPPED = 1


class Flip(Enum):
    UNFLIPPED = 0
    FLIPPED = 1


class Facing(Enum):
    FACE_UP = 0
    FACE_DOWN = 1


class Phasing(Enum):
    PHASED_IN = 0
    PHASED_OUT = 1


class Status:
    def __init__(self):
        self.tap = Tap.UNTAPPED
        self.flip = Flip.UNFLIPPED
        self.facing = Facing.FACE_UP
        self.phasing = Phasing.PHASED_IN
