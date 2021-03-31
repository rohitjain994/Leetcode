# arr = [ 10, 4, 2, 20, 40, 12, 30 ]
# res = [ -1, 10, 4, -1, -1, 40, 40 ]
def previousGreaterElement(arr : List[int])-> List[int]:
    stack = [arr[0]]
    res = [-1]
    for i in range(1,len(arr)):
        while len(stack)>0 and stack[-1]<arr[i]:
            stack.pop()
        if len(stack)==0:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(arr[i])
    return res
