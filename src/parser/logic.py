from src.constants import SYMBOLS

def IMPLIES(A : bool, B : bool) -> bool:
    """
    if A, then B ... logically equivalent to not A or B.
    True when "not A or B" is True, False otherwise
    """
    return (not A) or B

def IFF(A : bool, B : bool) -> bool:
    """
    Goal: A if and only if B
    True when
    "not A or B" and "not B or A" is True,
    False otherwise
    """
    return IMPLIES(A, B) and IMPLIES(B, A)

def AND(A : bool, B : bool) -> bool:
    """
    True when both of A, B are of truthy values,
    False otherwise
    """
    return A and B

def OR(A : bool, B : bool) -> bool:
    """
    True when at least one of A, B have a truthy value,
    False otherwise
    """
    return A or B

def XOR(A : bool, B : bool) -> bool:
    """
    True when only one of A or B is True.
    False otherwise
    """
    return A ^ B

def NOT(A : bool) -> bool:
    """
    True when A is False,
    False otherwise
    """
    return not A

BOOLEANS = {
            SYMBOLS["LOGICAL"]["TRUE"]:True,
            SYMBOLS["LOGICAL"]["FALSE"]:False
            }