def prefixToPostfix(s:str)->None:
    stack = []
    s = s[::-1]
    op = set(['+','-','*','/','^'])
    for i in s:
        if i in op:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b+i)
        else:
            stack.append(i)
    print(stack)
