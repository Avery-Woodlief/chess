import random
from logs.logger import Logger
from logs.exceptions import PositionError, PositionLengthError

HEX_CHARS = "0123456789abcdef"

def generate_id(piece_type : str, team : int, digits=5) -> str:

    if piece_type == "":
        piece_type = "None"

    if team == -1:
        team = "None"

    id_ = "".join(random.choices(HEX_CHARS, k=digits))
    while f"{piece_type}-{id_}-{team}" in Piece.in_play.keys():
        id_ = "".join(random.choices(HEX_CHARS, k=digits))
    full_id = f"{piece_type}-{id_}-{team}"
    return full_id

from src.geometry.position import Position
from src.file_utilities.file_navigator import FileNavigator

class Piece:
    in_play = dict()
    def __init__(self, piece_type="", team=-1, x=0, y=0):
        self.id = generate_id(piece_type, team)
        self.team = team if team != -1 else None
        self.type = piece_type
        Piece.in_play[self.id] = self
        self.position = Position(x, y)
        self.moves_made = 0 # has not made a move yet, off
        self.path = {}
        self.path["initial"] = (self.position.x, self.position.y)

    @property
    def class_name(self):
        return type(self).__name__

    @property
    def details(self):
        dets = dict()
        for name, thing in self.__dict__.items():
            if not callable(thing) and hasattr(self, name):
                dets[name] = str(getattr(self, name))
        return dets

    def move(self, destination):
        try:
            self.position = Position(destination[0], destination[1])
            self.moves_made += 1
            self.path[self.moves_made] = (self.position.x, self.position.y)


        except PositionError as e:
            Logger.write_to_logs(e, "failed to move piece")

    def __eq__(self, other):
        if hasattr(other, "id"):
            if self.id == other.id:
                return True
        return False

    def __str__(self):
        return f"type:{str(self.type)},id:{self.id}"
