from src.game_pieces.piece import Piece
from src.binding_functions import *
from src.constants import SYMBOLS
from logs.exceptions import *
import re
from src.parser.regex_maker import compile_specs_pattern, compile_action

class Board:
    selected_id = None
    selected_rules = None
    def __init__(self, length = 7, width = 7):
        self.length = length
        self.width = width
        self.squares = [[None for i in range(self.length)] for j in range(self.width)]
    @staticmethod
    def execute_selected_piece_tokens():
        value_bind_pattern = compile_specs_pattern()
        action_pattern = compile_action()
        for token in Board.selected_rules:
            print(action_pattern.search(token))
            print(token)



    @staticmethod
    def remove_piece(piece : Piece):
        if Piece.in_play.get(piece.id):
            del Piece.in_play[piece.id]

    @staticmethod
    def GET_DESTINATION_RANGE(direction: str, value : str) -> list:
        """
        returns a list of destinations:
            lower bound destination
            upper bound destination (if available)
        """
        direction_from_symbols = SYMBOLS["DIRECTIONS"].get(direction.upper())
        if not direction_from_symbols:
            raise InvalidTokenError("bad DIRECTIONS token")
        range = re.findall(r"\d+", value)
        lower_bound = None
        upper_bound = None
        return_range = []
        if not range:
            raise InvalidTokenError("bad VALUE token argument(s)")

        effect = direction_from_symbols["effect"]


        lower_bound = Position(int(range[0]) * effect[0], int(range[0]) * effect[1])

        return_range.append(lower_bound)
        if len(range) > 1:
            upper_bound = Position(int(range[1]) * effect[0], int(range[1]) * effect[1])
            return_range.append(upper_bound)
        return return_range

    @staticmethod
    def MOVE(piece : Piece, destination):
        """
        wrapper for moving the Piece instance to destination
        """
        piece.move(destination)
