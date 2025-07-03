from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = prerequisites
        # Step 1: Build the graph
        g = defaultdict(list)
        for a,b in courses:
            g[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        # DFS function to detect cycle
        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True # Already checked, no cylce here
            elif state == VISITING:
                return False # Found a cycle
            
            # Mark course as visiting
            states[node] = VISITING

            # Visit all prerequisites of this course
            for nei in g[node]:
                if not dfs(nei):
                    return False # Found a cycle

            # After all prereqs are safe, mark as visited
            states[node] = VISITED
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

        # TC: O(N+E) N = numCourses, E = total prereqs
        # SC: O(N+E)