# '(){}[]'를 포함하고 있는 문자열 s가 주어졌을 때, 괄호가 유효한지 아닌지 판별하시요.

# 제약조건
# 1 <= s.length <= 10^4
# 문자열 s는 '(){}[]'의 괄호 들로만 구성되어 있다.

# 10^8을 넘기면 안됨 -> n^2은 안됨

def isValid(s):
    stack = []
    for v in s:
        if v == '(':
            stack.append(')')
        elif v == '{':
            stack.append('}')
        elif v == '[':
            stack.append(']')
        elif not stack or stack.pop() != v:
            return False
    return not stack
