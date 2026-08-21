import re

value_bind = r'''
(?P<variable>\w+\s*)?
\[
\s*
(?:VALUE\s*:\s*)?
(?P<value>\d+(?:\.\.\d+)?)
\s*,\s*
(?:BIND\s*:\s*)?
(?P<bind>\w+)
\s*,\s*
(?:CONTEXT\s*:\s*)?
(?P<context>\w+)
\]'''

def compile_condition(flags=re.VERBOSE) -> re.Pattern[str]:
    return re.compile(r"(?<=\().*(?=\))", flags=flags)

def compile_binary_operation(operation="AND", flags=re.VERBOSE) -> re.Pattern[str]:
    return re.compile(rf'''(?P<LHS>\(.*\))\s*{operation.upper()}\s*(?P<RHS>\(.*\))''', flags=flags)

def compile_unary_operation(operation="NOT", flags=re.VERBOSE) -> re.Pattern[str]:
    return re.compile(rf'''{operation}\s*(?P<RHS>\(.*\))''', flags=flags)


if __name__ == "__main__":
    condition = compile_condition()
    QUERY = "(MOVES_MADE[VALUE:0, BIND:moves_made, CONTEXT:self]) AND (EMPTY AT NORTH[VALUE:1..2, BIND:distance, CONTEXT:global])"
    conditions = condition.split(QUERY)
    print(conditions)
    AND = compile_binary_operation("and")
    print(AND.search(QUERY).groupdict())
    NOT = compile_unary_operation()
    value_bind_pattern = re.compile(value_bind, re.X)
    if value_bind_pattern.search(QUERY):
        print(value_bind_pattern.search(QUERY).groupdict())