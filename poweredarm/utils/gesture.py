from enum import Enum, unique

@unique
# Gestures stored in csv as integers: rest -> 0, grip -> 1, flex -> 2
class Gesture(Enum):
    Rest = 0
    Grip = 1
    Flex = 2
    #TODO Key

