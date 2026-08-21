from src.game_pieces.board import *

if __name__ == "__main__":
    board = Board()
    pawn = Piece("pawn", team=0, x=0, y=1) # selected piece
    print(Piece.in_play.get(pawn.id))

    board.squares[pawn.position.y][pawn.position.x] = str(pawn)
    for row in board.squares:
        print(row)

    Board.remove_piece(pawn)
    print(Piece.in_play.get(pawn.id))