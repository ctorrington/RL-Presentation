"""
Constants.
"""

from enum import Enum

class Constants:

    class ACTIONS(Enum):
        UP = "UP"
        DOWN = "DOWN"
        LEFT = "LEFT"
        RIGHT = "RIGHT"

        @staticmethod
        def as_tuple():
            return Constants.ACTIONS.UP, Constants.ACTIONS.DOWN, Constants.ACTIONS.LEFT, Constants.ACTIONS.RIGHT