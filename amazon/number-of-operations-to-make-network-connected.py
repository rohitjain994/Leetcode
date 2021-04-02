class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: return -1
        graph = collections.defaultdict(list)
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)
        def dfs(node):
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    dfs(i)
        cnt = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt+=1
        return cnt-1        
        