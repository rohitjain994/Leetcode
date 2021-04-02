class Solution:
    def isValid(self, s: str) -> bool:
        dmap = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i in dmap and stack and stack[-1] == dmap[i]:
                stack.pop()
            else:
                stack.append(i)
        # print(stack)
        return not stack
        