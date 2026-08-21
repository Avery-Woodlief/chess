from src.game_pieces.board import *

def tokenize_statement(statement:str)->list:
    tokens = statement.split(";")
    while '' in tokens:
        tokens.remove('')
    tokens_ = []
    for token in tokens:
        tokens_.append(token.strip(' '))
    return tokens_

if __name__ == "__main__":
    pawn = Piece("pawn", 0, 0, 1)
    Board.selected_id = pawn.id
    Board.selected_rules = tokenize_statement(pawn.normal_rule["ACTION"])
    Board.execute_selected_piece_tokens()