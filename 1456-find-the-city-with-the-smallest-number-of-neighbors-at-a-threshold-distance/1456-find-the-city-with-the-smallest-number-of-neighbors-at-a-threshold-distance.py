class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')]*n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0
        
        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[j][k]:
                        dist[i][j] = dist[i][k] + dist[j][k]
        
        minReachCity = float('inf')
        bestCity = -1

        for i in range(n):
            reachable_cities = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    reachable_cities += 1
            
            if reachable_cities <= minReachCity:
                minReachCity = reachable_cities
                bestCity = i
        
        return bestCity