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

# with Lambda 
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        sorting = {e:i for i, e in enumerate(order)}
        return words == sorted(words, key = lambda x: [sorting[c] for c in x])

# With comparator
class Solution:
	def isAlienSorted(self, words: List[str], order: str) -> bool:
        D = {e:i for i,e in enumerate(order)}
        def comparator(x1, x2):
            for i in range(min(len(x1), len(x2))):
                if x1[i] != x2[i]:
                    return -1 if D[x1[i]] < D[x2[i]] else 1
            if len(x1) == len(x2):
                return 0
            return -1 if len(x1) < len(x2) else 1
        return words == sorted(words, key = functools.cmp_to_key(comparator))