from src.game_pieces.piece import Piece
from logs.exceptions import BoardError, BoardDimensionError, BoardObjectError
from typing import Any

class Board:
    def __init__(self, width : int, length : int):
        self.width = width
        self.length = length
        self.squares = [[None for i in range(width)] for j in range(length)]

    def __getitem__(self, row : int) -> list[Any]:
        if isinstance(row, int) and (row >= 0 and row < self.length):
            return self.squares[row]

        raise BoardDimensionError("bad row value")
    def __setitem__(self, position : tuple[int], item : Any) -> None:
        if not isinstance(position, tuple):
            raise TypeError("position not tuple")
        row = position[0] # corresponds with the x position of Piece
        col = position[1] # corresponds with the y position of Piece
        if not isinstance(item, Piece):
            raise BoardObjectError(f"In position ({row}, {col}), got {type(item)}.\nExpected {Piece}")
        self.squares[row][col] = item
        #item.move(position)

    @property
    def class_name(self):
        return type(self).__name__




if __name__ == "__main__":
    board = Board(3, 4)
    pawn = Piece("pawn", x=1, y=2)
    board[(1, 2)] = pawn
    print(board[pawn.position.x][pawn.position.y])