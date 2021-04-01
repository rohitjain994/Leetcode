# from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)
        # for i in strs:
        #     m["".join(sorted(i))].append(i)
        # res = []
        # for i in m.values():
        #     i.sort()
        #     res.append(i)
        # res.sort(key=len)
        # return res
        for s in strs:
            m[tuple(sorted(s))].append(s)
        return m.values()
            