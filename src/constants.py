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
        #"CONDITION": "\u25C7",    # ◇ # NOT NEEDED

        "ACTION_OPEN": "[",
        "ACTION_CLOSE": "]",

        "CONDITION_OPEN": "(",
        "CONDITION_CLOSE": ")"#,

        #"PIECE_OPEN": "<", # NOT NEEDED
        #"PIECE_CLOSE": ">", # NOT NEEDED

        #"QUANTITY_OPEN": "{", # NOT NEEDED
        #"QUANTITY_CLOSE": "}", # NOT NEEDED
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
NOTE:
    the context of variables under either CONDITION, ATTACK, or SPECIAL is the Piece instance that is currently selected

GRAMMAR:
    \d+..\d+        indicates a range of numbers from \d+ to \d+
                        upper bound of range is always one of the following:
                            (1) destination square selected via user input
                            (2) board bounds
                            
    (...)       ... indicates a condition to be looked at and queried, 
                        used to help group operands for logical operations
  
    $...$       ... indicates a non-token variable that is assumed to be a class member of Piece
  
    [...]       goes with either $....$[...] to help group properties and behavior hints for $....$
                          or ....[...]       to help group properties and behavior hints for ....

KEYWORDS:
    VALUE           followed by a ':' and either a single number or a range indicated by 
                        either a..b or c, where a, b, and c are positive integers
                        
    BIND            followed by a ':' and a behavior hint, that is, the name of the function that is to be used
                        as the metric
                        If the named metric is not defined then that instruction is invalid and will be skipped (or crash)
                        valid binding functions are found in src.binding_functions.py
                        
    DIRECTIONS      each DIRECTION keyword is used in the following format
                        DIRECTION[VALUE: ..., BIND:....]
    MOVE            must be followed by one of the DIRECTION keywords
    
    EMPTY           indicates that at least one of the board squares needs to be empty, the instructions which follow are
                        AT DIRECTION[VALUE:a, BIND:func_name]

CONDITION:
    any value mapping to this key is to be queried
    
ACTION:
    instructions for how the Piece instance is to MOVE and what DIRECTION
    


PARENT CATEGORIES: (NOTE: all parent categories only use CONDITION and an ACTION. If multiple then must be put into a list)
    NORMAL          instructions under ordinary movement of the Piece instance
    
    CAPTURING       instructions for how and when the Piece instance can capture an enemy piece
    
    SPECIAL         instructions for how and when to do a non-ordinary move that is not a capture, 
                        examples include (not limited to): castling, pawn promotion, check, etc...
"""