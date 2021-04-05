class Solution:
    def countBits(self, num: int) -> List[int]:
        p = [0,1]
        if num==0:
            return [0]
        i,j,cnt=0,2,2
        while j<=num:
            if i<cnt:
                p.append(p[i]+1)
                i+=1
                j+=1
            else:
                i=0
                cnt=j
        return p
#  00  0
#  01  1
# 10   1
# 11   2
# 100. 1
# 101. 2
# 110. 2
# 111. 3