def is_valid_parenthesis(s):
    stk = []
    for ch in s:
        if ch in ('(', '{', '['):
            stk.append(ch)
        else:
            if stk and ((stk[-1] == '(' and ch == ')') or
                          (stk[-1] == '{' and ch == '}') or
                          (stk[-1] == '[' and ch == ']')):
                stk.pop()
            else:
                return False
    return not stk

expr = "({()}[])"

# Function call
op=is_valid_parenthesis(expr)
print(op)
