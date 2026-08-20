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

        "NORTHEAST": {
            "label": "NE",
            "effect": (1, 1),
        },
        "NORTHWEST": {
            "label": "NW",
            "effect": (-1, 1),
        },
        "SOUTHEAST": {
            "label": "SE",
            "effect": (1, -1),
        },
        "SOUTHWEST": {
            "label": "SW",
            "effect": (-1, -1),
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
    "ACTIONS": {
        "MOVE": "\u2192",
        "CAPTURE": "\xd7",
        "PROMOTE": "\u21D1",
        "CASTLE": "\u21c6",
        "EN_PASSANT": "\u2198",
        "HALT": "\u25A0",         # ■
    },
    "STATE": {
        "IN_MOTION": "\u219D",    # ↝
        "INITIAL": "\u25C9",      # ◉
        "NORMAL": "\u25CB",       # ○
        "CAPTURING": "\u2717",    # ×
        "SPECIAL": "\u2605",      # ★

        "SELECTED": "\u24c8", # Ⓢ
        "CAPTURED": "\u2620", # ☠
        "IN_CHECK": "\u203C", # ‼
    },
    "BOARD": {
        "SQUARE": "\u25A1",       # □
        "ADJACENT": "\u223C",     # ∼
        "AT": "\u0040",           # @
        "EMPTY": "\u2205",        # ∅
        "FRIENDLY": "\u2299",     # ⊙
        "ENEMY": "\u2297",        # ⊗
        "END_OF_BOARD": "\u22A3", # ⊣

        "PATH_CLEAR": "CLEAR",
        "BLOCKED": "BLOCKED",
        "ATTACKED": "\u2694", # ⚔
    },
    "GRAMMAR": {
        "RANGE": "..",
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
    "SPECIAL_RULES": {
        "CASTLING": "CASTLING",
        "KINGSIDE": "KINGSIDE",
        "QUEENSIDE": "QUEENSIDE",
        "EN_PASSANT": "EN_PASSANT",
        "LAST_MOVE": "LAST_MOVE",
    }
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