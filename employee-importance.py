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
            return emp[idx].importance + sum(dfs(i) for i in emp[idx].subordinates)
        return dfs(id)
        
