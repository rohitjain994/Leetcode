def nextGreator(arr: List[int]) -> List[int]:
    stack = [arr[0]]
    res = []
    for i in range(1,len(arr)):
        if len(stack)==0:
            stack.append(arr[i])
            continue
        while len(stack)>0 and stack[-1]<arr[i]:
            res.append(arr[i])
            stack.pop()
        stack.append(arr[i])
    while len(stack)>0:
        res.append(-1)
        stack.pop()
    return res