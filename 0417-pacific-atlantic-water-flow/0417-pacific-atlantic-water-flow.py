from collections import defaultdict
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Visited set for both oceans, and queue
        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        m , n = len(heights), len(heights[0]) # m = rows, n = columns

        # Initializing pacific queue with top row and left column
        for i in range(n):
            p_que.append((0,i))
            p_seen.add((0,i))
        
        for j in range(1,m):
            p_que.append((j,0))
            p_seen.add((j,0))
        
        # Initializing atlantic queue with bottom row and right column
        for i in range(n):
            a_que.append((m-1,i))
            a_seen.add((m-1,i))
        
        for j in range(m-1):
            a_que.append((j,n-1))
            a_seen.add((j,n-1))
        
        # BFS function to get co-ords of the neighbouring cells
        def bfs(queue,seen):   
            while queue:
                i,j = queue.popleft()
                for i_off,j_off in [(0,1),(0,-1),(1,0),(-1,0)]:
                    r,c = i + i_off, j + j_off
                    # Check bounds and whether water can flow from r,c to i,j
                    if r >= 0 and r < m and c >= 0 and c < n and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        queue.append((r,c))
                        seen.add((r,c))

         

        
        # Run BFS from pacific and atlantic, and get coordinates that can reach their respective ocean
        p_coords = bfs(p_que,p_seen)
        a_coords = bfs(a_que,a_seen)

        # We will return a list of that intersection
        return list(p_seen.intersection(a_seen))

        # TC: O(m*n) Each cell is visited atmost twice
        # SC: O(m*n) 
        


