"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {e.id:e for e in employees}
        def dfs(idx):
            res = emp[idx].importance
            for i in emp[idx].subordinates:
                res+=dfs(i)
            return res
        return dfs(id)
