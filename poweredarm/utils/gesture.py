from enum import Enum, unique

@unique
# Gestures stored in csv as integers: rest -> 0, grip -> 1, and so forth
class Gesture(Enum):
    Rest = 0
    Grip = 1
    Open = 2
    Key = 3

