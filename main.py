from src.file_utilities.file_navigator import FileNavigator
from src.constants import SYMBOLS



if __name__ == "__main__":
    game_rules = FileNavigator.grab("rules", "behavior.json")

    DIRECTIONS = SYMBOLS["DIRECTIONS"]
    PIECES = SYMBOLS["PIECES"]
    LOGICAL = SYMBOLS["LOGICAL"]
    GRAMMAR = SYMBOLS["GRAMMAR"]
    STATE = SYMBOLS["STATE"]
    BOARD = SYMBOLS["BOARD"]

    TOKEN_GROUPS = (
        DIRECTIONS,
        PIECES,
        LOGICAL,
        GRAMMAR,
        STATE,
        BOARD,
    )


    def fetch_token(token):
        for group in TOKEN_GROUPS:

            if token not in group:
                continue

            value = group[token]

            # Directions are dictionaries like:
            # {"label": "N", "effect": (0, 1)}
            if isinstance(value, dict):
                return value["label"]

            return value

        raise KeyError(f"Unknown token: {token}")


    def build_expression(rule):
        expression = ""

        for token in rule:
            if isinstance(token, dict):
                expression += str(token["VALUE"])
            else:
                expression += fetch_token(token)

        return expression


    normal_condition = game_rules["PAWN"]["NORMAL"][1]["CONDITION"]
    normal_movement = game_rules["PAWN"]["NORMAL"][1]["ACTION"]

    normal_condition_expression = build_expression(normal_condition)
    normal_movement_expression = build_expression(normal_movement)

    print(f"if {normal_condition_expression}, then {normal_movement_expression}")