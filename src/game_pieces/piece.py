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
        self.type = piece_type
        Piece.in_play[self.id] = self
        self.position = Position(x, y)
        self.moves_made = 0 # has not made a move yet
        self.path = []
        self.vars_mapping = {"MOVES_MADE":self.moves_made, "MOVE":self.move}

    def move(self, destination):
        try:
            self.position = destination
        except PositionError as e:
            Logger.write_to_logs(e, "failed to move piece")

    def __eq__(self, other):
        if hasattr(other, "id"):
            if self.id == other.id:
                return True
        return False

    def __str__(self):
        return f"type:{str(self.type)},id:{self.id}"
