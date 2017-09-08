def parse():
    token = ""
    tokens = []
    state = 0
    script = open("script.stl", "r").read()
    for char in script:
        if char == "\"" and state != 2:
            if state:
                state = 0
                continue
            else:
                state = 1
                continue
        if char == "'" and state != 1:
            if state:
                state = 0
                continue
            else:
                state = 2
                continue
        if (char != " " and char != "\n") or state:
            token += char
        elif not state:
            tokens.append(token)
            token = ""
    return (tokens)

def lex(tok):
    stack = []
    i = 0
    while i < len(tok):
        if tok[i] == "PUSH":
            stack.append(float(tok[i + 1]))
        elif tok[i] == "SUM":
            num = stack[-1]
            del stack[-1]
            stack[-1] += num
        elif tok[i] == "INC":
            stack[-1] += 1
        elif tok[i] == "DEC":
            stack[-1] -= 1
        elif tok[i] == "POP":
            del stack[-1]
        elif tok[i] == "REV":
            stack = stack[::-1]
        elif tok[i] == "IF":
            if stack[-1] != float(tok[i + 1]):
                i += 2
        elif tok[i] == "NOT":
            if stack[-1] == float(tok[i + 1]):
                i += 2
        elif tok[i] == "OUT":
            if int(stack[-1]) == stack[-1]:
                print(int(stack[-1]))
            else:
                print(stack[-1])
        i += 1

tokens = parse()
lex(tokens)
