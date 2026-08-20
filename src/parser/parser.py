import re
from src.constants import SYMBOLS

value_bind = r'''(?P<variable>\w+\s*)?
\[
\s*
(?:VALUE\s*:\s*)?
(?P<value>\d+(?:\.\.\d+)?)
,\s*
(?:BIND\s*:\s*)?
(?P<bind>\w+)
\]'''

class Parser:
    pass