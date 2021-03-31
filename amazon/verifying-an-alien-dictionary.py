class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        odr = collections.defaultdict(int)
        for i,s in enumerate(order):
            odr[s] = i
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >=len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if odr[words[i][j]] > odr[words[i+1][j]]:
                        return False
                    break
        return True