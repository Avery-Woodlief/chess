from src.game_pieces.piece import Piece
from src.binding_functions import *
from src.constants import SYMBOLS
from logs.exceptions import *
import re

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

def MOVE(piece : Piece, destination):
    """
    wrapper for moving the Piece instance to destination
    """
    piece.move(destination)

if __name__ == "__main__":
    pawn = Piece("pawn", team=0, x=0, y=0) # selected piece
    ACTION = pawn.normal_rule["ACTION"]
    print(ACTION.split(";"))
    destination_ranges = GET_DESTINATION_RANGE("NORTH", "1..2")
    for d_range in destination_ranges:
        MOVE(pawn, d_range)
        print(d_range)
    print(pawn.position)