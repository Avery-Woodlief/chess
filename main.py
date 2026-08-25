from src.file_utilities.file_navigator import FileNavigator
from src.game_pieces.piece import Piece
from src.game_pieces.board import Board
from src.lua_wrapper.lua_executor import resolve_lua
from logs.logger import ChessLogger, logging

logs = ChessLogger()
if __name__ == "__main__":

    board = Board(7, 7)
    logs.log(area="initialization",
             message="created game board",
             level=logging.INFO)

    pawn = Piece("pawn", team=0, x=1,y=3)
    logs.log(area="initialization",
             message="created pawn for team 0",
             level=logging.INFO)
    enemy_pawn = Piece("pawn", team=1, x=0, y=3)
    logs.log(area="initialization",
             message="created pawn for team 1",
             level=logging.INFO)
    board[(1, 3)] = pawn
    board[(0, 4)] = enemy_pawn
    logs.log(area="initialization",
             message="put pawns on board",
             level=logging.INFO)
    print(pawn.details)
    print(enemy_pawn.details)

    _tuple = lambda *args: tuple(args)
    lua = resolve_lua(board=board, tuple=_tuple)
    logs.log(area="initialization",
             message="grabbed lua code",
             level=logging.INFO)
    #lua.globals().board = board

    lua.execute(FileNavigator.grab("lua/rules", "pawn.lua"))
    normal_move = lua.globals().normal_move
    move_report = normal_move(pawn, (1, 4))
    logs.log(area="MOVEMENT",
             message=f"generated move report for {pawn} to (1, 4)",
             level=logging.INFO)
    if move_report["legal_move"]:
        pawn.move(move_report["destination"])
        print(pawn.details)
        print(enemy_pawn.details)
        logs.log(area="MOVEMENT",
             message=f"successfully moved {pawn} to (1, 4)",
             level=logging.INFO)
    else:
        print(move_report["validation_response"])
        print(move_report["destination_response"])
        logs.log(area="MOVEMENT",
             message=f"could not move {pawn} to (1, 4) because it was illegal\nVALIDATION RESPONSE:{move_report['validation_response']}\nDESTINATION RESPONSE: {move_report['destination_response']}",
             level=logging.INFO)

    capture_move = lua.globals().capture_move
    capture_report = capture_move(pawn, enemy_pawn)

    print(capture_report["validation_response"])