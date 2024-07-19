class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        columns = len(matrix[0])
        res = []
        row_min = set()

        for r in range(rows):
            row_min.add(min(matrix[r]))
        
        col_max = set()

        for c in range(columns):
            cur_max = matrix[0][c]
            for r in range(rows):
                cur_max = max(cur_max, matrix[r][c])
            col_max.add(cur_max)
        
        
        for n in row_min:
            if n in col_max:
                res.append(n)
        
        return res
