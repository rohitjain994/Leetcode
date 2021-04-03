class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c:i for i,c in enumerate(S)}
        j = ac = 0
        res = []
        for i,c in enumerate(S):
            j = max(j,last[c])
            if j==i:
                res.append(i-ac+1)
                ac = i+1
        return res