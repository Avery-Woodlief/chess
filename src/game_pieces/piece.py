import random
from src.constants import HEX_CHARS

def generate_id(piece_type : str, team : int, digits=4) -> str:

    if piece_type == "":
        piece_type = "None"

    if team == -1:
        team = "None"

    id_ = "".join(random.choices(HEX_CHARS, k=digits))
    while f"{piece_type}-{id_}" in Piece.ids_in_play:
        id_ = "".join(random.choices(HEX_CHARS, k=digits))
    full_id = f"{piece_type}-{id_}-{team}"
    return full_id

class Piece:
    ids_in_play = set()
    def __init__(self, piece_type="", team=-1):
        self.id = generate_id(piece_type, team)
        Piece.ids_in_play.add(self.id)

    def __str__(self):
        return self.id


if __name__ == "__main__":
    pawns = [Piece("pawn", i % 2) for i in range(16)]
    kings = [Piece("king", i % 2) for i in range(2)]
    queens = [Piece("queen", i % 2) for i in range(2)]
    rooks = [Piece("rooks", i % 2) for i in range(2)]
    knights = [Piece("knights", i % 2) for i in range(2)]
    bishops = [Piece("bishops", i % 2) for i in range(2)]

    for p in pawns+kings+queens+rooks+knights+bishops:
        print(p)
    print(len(list(set(Piece.ids_in_play))))