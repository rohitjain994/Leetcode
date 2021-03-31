def postfixToInfix(s:str)->None:
    stack = []
    op = set(['+','-','*','/','^'])
    for i in s:
        if i in op:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+i+b)
        else:
            stack.append(i)
    print(stack)
