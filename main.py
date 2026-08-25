from src.file_utilities.file_navigator import FileNavigator
from src.game_pieces.piece import Piece
from src.game_pieces.board import Board
from src.lua_wrapper.lua_executor import resolve_lua
from logs.logger import ChessLogger, logging

if __name__ == "__main__":

    board = Board(7, 7)

    pawn = Piece("pawn", team=0, x=1,y=3)
    enemy_pawn = Piece("pawn", team=1, x=0, y=3)
    board[(1, 3)] = pawn
    board[(0, 4)] = enemy_pawn
    print(pawn.details)
    print(enemy_pawn.details)

    _tuple = lambda *args: tuple(args)
    lua = resolve_lua(board=board, tuple=_tuple)
    #lua.globals().board = board

    lua.execute(FileNavigator.grab("lua/rules", "pawn.lua"))
    normal_move = lua.globals().normal_move
    move_report = normal_move(pawn, (1, 4))
    if move_report["legal_move"]:
        pawn.move(move_report["destination"])
        print(pawn.details)
        print(enemy_pawn.details)
    else:
        print(move_report["validation_response"])
        print(move_report["destination_response"])

    capture_move = lua.globals().capture_move
    capture_report = capture_move(pawn, enemy_pawn)

    print(capture_report["validation_response"])