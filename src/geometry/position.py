from logs.exceptions import PositionError
from typing import Any

def type_check(other, additional_msg):
        if not isinstance(other, (Position, tuple, list)):
            raise PositionError(f"argument named other is not type Position, tuple, list.\ngot {type(other)}\n{additional_msg}")
        return None

class Position:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y



    def __add__(self, other):
        type_check(other, f"could not do {self}+{other}\ntypes: {type(self)}, {type(other)}")
        if isinstance(other, (list, tuple)):
            return Position((self.x + other[0]), (self.y + other[1]))
        return Position((self.x + other.x), (self.y + other.y))

    def __eq__(self, other: Any):
        type_check(other, f"could not do {self}=={other}\ntypes: {type(self)}, {type(other)}")
        if isinstance(other, (list, tuple)):
            return (self.x == other[0]) and (self.y == other[1])
        return (self.x == other.x) and (self.y == other.y)
    def __str__(self):
        return f"{self.x}, {self.y}"

if __name__ == "__main__":
    try:
        print(Position(0, 0) + {1, 2})
    except Exception as e:
        from logs.logger import Logger
        Logger.write_to_logs(e, "")