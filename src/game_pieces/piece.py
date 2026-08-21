import random
from src.constants import HEX_CHARS
from logs.logger import Logger
from logs.exceptions import PositionError, PositionLengthError
from src.constants import SYMBOLS


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
        self.rule_set = FileNavigator.grab("rules", f"{piece_type}.json")
        if not self.rule_set:
            self.rule_set = dict()
        self.normal_rule = self.rules("NORMAL")
        self.capturing_rule = self.rules("CAPTURING")
        self.special_rule = self.rules("SPECIAL")
        self.moves_made = 0 # has not made a move yet
        self.path = []
        self.vars_mapping = {"MOVES_MADE":self.moves_made, "MOVE":self.move}

    def move(self, destination):
        try:
            self.position = destination
        except PositionError as e:
            Logger.write_to_logs(e, "failed to move piece")

    def rules(self, category):
        return self.rule_set.get(f"{category}".upper())

    def __eq__(self, other):
        if hasattr(other, "id"):
            if self.id == other.id:
                return True
        return False

    def __str__(self):
        return SYMBOLS["PIECES"].get(str(self.type).upper())
