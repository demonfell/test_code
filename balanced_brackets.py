def balanced_brackets(s):
    brackets = {'(': ')', '[': ']', '{':'}'}
    stack = []
    for c in s:
        if c in brackets:
            stack.append(c)
        elif c in list(brackets.values()):
            if not stack:
                return False
            opener = stack.pop()
            expected = brackets[opener]
            if expected != c: 
                return False
    # if not stack:
    #    return True
    # else:
    #    return False
    # better way below
    # if you want a true or false value, could use bool on stack
    return not stack

print(balanced_brackets('{}}'))
