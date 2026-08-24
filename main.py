from src.file_utilities.file_navigator import FileNavigator
from src.game_pieces.piece import Piece
from src.game_pieces.board import Board
from src.lua_wrapper.lua_executor import resolve_lua
from logs.exceptions import *
from logs.logger import Logger

if __name__ == "__main__":
    board = Board(7, 7)

    pawn = Piece("pawn", team=0, x=0,y=0)
    board[(1, 2)] = pawn
    print(pawn.details)


    lua = resolve_lua(board=board)
    #lua.globals().board = board

    lua.execute(FileNavigator.grab("lua/rules", "pawn.lua"))
    normal_move = lua.globals().normal_move
    move_report = normal_move(pawn, (0, 2))
    if move_report["legal_move"]:
        pawn.move(move_report["destination"])
        print(pawn.details)
    else:
        print(move_report["destination_response"])