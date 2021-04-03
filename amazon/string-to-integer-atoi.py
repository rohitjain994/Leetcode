class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        f = 1
        try:
            i = 0
            while s[i] == ' ':
                i+=1
            if s[i] == '-':
                f = -1
                i+=1
            elif s[i] == '+':
                i+=1
            while '0'<=s[i]<='9':
                res = res*10 + int(s[i])
                i+=1
        finally:
            return min(max(f*res,-2**31),2**31-1)
