class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE, GREY, BLACK = 0, 1, 2
        graph, colors = {}, {}
        
        for i in range(numCourses):
            graph[i] = []
            colors[i] = WHITE
        for x,y in prerequisites:
            graph[x].append(y)
        # Graph colors to detect cycle  in directed graph  
        def dfs(node):
            if colors[node] == BLACK: return True
            if colors[node] == GREY: return False
            colors[node] = GREY
            for neighbor in graph[node]:
                if not dfs(neighbor): return False
            colors[node] = BLACK
            return True
        
        for node in graph:
            if not dfs(node): return False
        return True
    
# Indgree  topological sort BFS

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indgree = [0]*numCourses
        graph = collections.defaultdict(list)
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
            indgree[pre[1]]+=1
        # print(graph,indgree)    
        que = []
        topo = []
        cnt = 0
        for i in range(numCourses):
            if indgree[i]==0:
                que.append(i)
        while len(que)>0:
            p = que.pop(0)
            topo.append(0)
            for i in graph[p]:
                indgree[i] -=1
                if indgree[i] == 0:
                    que.append(i)
            cnt += 1
        # print(topo)
        if cnt == numCourses:
            return True
        return False
            