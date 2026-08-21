class InvalidBindError(Exception):
    """Exception for bind checking"""
    pass

class PositionError(Exception):
    """Exception for the Position class"""
    pass

class PositionLengthError(Exception):
    """Exception for the Position class"""
    pass

class TokenError(Exception):
    """Exception for token handling"""
    pass

class InvalidTokenError(TokenError):
    """Exception for invalid tokens"""
    pass