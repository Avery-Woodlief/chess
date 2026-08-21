import math
from typing import Any
from src.geometry.position import Position
from logs.logger import Logger

def distance(P : Any, Q : Any) -> int | None:
    if isinstance(P, Position):
        P = (P.x, P.y)
    if isinstance(Q, Position):
        Q = (Q.x, Q.y)

    dist = None
    try:
        dist = int(math.dist(P, Q))
        return dist
    except Exception as e:
       Logger.write_to_logs(e, "math.dist failed")
       return None


VALID_BINDING_FUNCTIONS = {"distance":distance}