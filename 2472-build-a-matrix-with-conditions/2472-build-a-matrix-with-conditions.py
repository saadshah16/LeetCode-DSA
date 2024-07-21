class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, adj, visit, path, order):
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei, adj, visit, path, order):
                    return False
            path.remove(src)
            order.append(src)
            return True


        def topo_sort(edges):
            adj = defaultdict(list)
            for src, dst in edges:
                adj[src].append(dst)
        
            visit, path = set(), set()
            order = []
            for src in range(1,k+1):
                if not dfs(src, adj, visit, path, order):
                    return []
            return order[::-1] #reverse

        row = topo_sort(rowConditions)
        col = topo_sort(colConditions)
        
        if len(row) < k or len(col) < k: return []
        ans = [[0]*k for _ in range(k)]
        row = {x : i for i, x in enumerate(row)}
        col = {x : j for j, x in enumerate(col)}
        for x in range(1, k+1): ans[row[x]][col[x]] = x
        return ans 