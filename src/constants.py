SYMBOLS = {
    "DIRECTIONS": {
        "NORTH": {
            "label": "N",
            "effect": (0, 1),
        },
        "SOUTH": {
            "label": "S",
            "effect": (0, -1),
        },
        "EAST": {
            "label": "E",
            "effect": (1, 0),
        },
        "WEST": {
            "label": "W",
            "effect": (-1, 0),
        },
    },

    "PIECES": {
        "PAWN": "<p>",
        "ROOK": "<r>",
        "KNIGHT": "<kn>",
        "BISHOP": "<b>",
        "KING": "<k>",
        "QUEEN": "<q>",
    },

    "LOGICAL": {
        "AND": "\u2227",          # ∧
        "OR": "\u2228",           # ∨
        "NOT": "\u00AC",          # ¬
        "XOR": "\u2295",          # ⊕
        "IMPLIES": "\u21D2",      # ⇒
        "IFF": "\u21D4",          # ⇔
        "TRUE": "\u22A4",         # ⊤
        "FALSE": "\u22A5",        # ⊥
    },

    "GRAMMAR": {
        "CONDITION": "\u25C7",    # ◇

        "ACTION_OPEN": "[",
        "ACTION_CLOSE": "]",

        "CONDITION_OPEN": "(",
        "CONDITION_CLOSE": ")",

        "PIECE_OPEN": "<",
        "PIECE_CLOSE": ">",

        "QUANTITY_OPEN": "{",
        "QUANTITY_CLOSE": "}",
    },

    "STATE": {
        "MOVEMENT": "\u2192",     # →
        "IN_MOTION": "\u219D",    # ↝

        "INITIAL": "\u25C9",      # ◉
        "NORMAL": "\u25CB",       # ○

        "CAPTURING": "\u00D7",    # ×

        "SPECIAL": "\u2605",      # ★
        "END_OF_BOARD": "\u22A3", # ⊣
        "PROMOTION": "\u21D1",    # ⇑

        "HALT": "\u25A0",         # ■
    },

    "BOARD": {
        "SQUARE": "\u25A1",       # □
        "ADJACENT": "\u223C",     # ∼
        "AT": "\u0040",           # @
        "EMPTY": "\u2205",        # ∅

        "FRIENDLY": "\u2299",     # ⊙
        "ENEMY": "\u2297",        # ⊗
    },
}

HEX_CHARS = "0123456789abcdef"


"""
Example:

Statement:
    If in the initial state AND currently in motion,
    then move north 2 spaces.

DSL:
    ◇(◉ ∧ ↝) ⇒ [→N{2}]

Equivalent conceptual Python:
    if INITIAL and IN_MOTION:
        piece.move(NORTH, 2)


Grammar:

    ◇(...)      condition
    [...]       action
    <...>       piece/type identifier
    {...}       quantity / magnitude

Operators:

    ∧           AND
    ∨           OR
    ¬           NOT
    ⊕           XOR
    ⇒           implies / then
    ⇔           iff

States / properties:

    ◉           initial
    ↝           currently in motion
    ○           normal
    ×           capturing
    ★           special
    ⊣           end of board
    ⇑           promotion
    ■           halt
    ⊙           friendly
    ⊗           enemy

Movement:

    →N{2}       move north 2 spaces
    
"""