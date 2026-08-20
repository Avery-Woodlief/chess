import random
import re
from src.constants import HEX_CHARS
from src.parser.parser import Parser

def generate_id(piece_type : str, team : int, digits=5) -> str:

    if piece_type == "":
        piece_type = "None"

    if team == -1:
        team = "None"

    id_ = "".join(random.choices(HEX_CHARS, k=digits))
    while f"{piece_type}-{id_}-{team}" in Piece.ids_in_play:
        id_ = "".join(random.choices(HEX_CHARS, k=digits))
    full_id = f"{piece_type}-{id_}-{team}"
    return full_id

from src.geometry.position import Position
from src.file_utilities.file_navigator import FileNavigator

class Piece:
    ids_in_play = set()
    def __init__(self, piece_type="", team=-1, x=0, y=0):
        self.id = generate_id(piece_type, team)
        Piece.ids_in_play.add(self.id)
        self.position = Position(x, y)
        self.rule_set = FileNavigator.grab("rules", f"{piece_type}.json")
        if not self.rule_set:
            self.rule_set = dict()
        self.normal_rule = self.rules("NORMAL")
        self.capturing_rule = self.rules("CAPTURING")
        self.special_rule = self.rules("SPECIAL")
        self.moves_made = 0 # has not made a move yet
        self.path = []

    def rules(self, category):
        return self.rule_set.get(f"{category}".upper())

    def __str__(self):
        return str((self.id, self.position, "has rules" if self.rule_set else "no rules applied"))
