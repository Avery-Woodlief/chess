class PositionError(Exception):
    """Exception for the Position class"""
    pass

class PositionLengthError(Exception):
    """Exception for the Position class"""
    pass

class BoardError(Exception):
    """Exception base class for the Board class"""
    pass

class BoardDimensionError(BoardError):
    """Exception for board dimensions such as length/width
    examples include index out of bounds or using negative numbers or type error like
    Board[1.0][2] instead of Board[1][2]"""
    pass

class BoardObjectError(BoardError):
    """Exception for when an object that is not of type Piece is placed onto the board"""
    pass