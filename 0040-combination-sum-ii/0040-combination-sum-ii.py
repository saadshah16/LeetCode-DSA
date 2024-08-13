class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res, sol = [], []
        self.backtrack(0,target,candidates,res,sol)
        return res

    def backtrack(self,idx,target,arr,res,sol):
            if target == 0:
                res.append(sol[:])
                return
            
            for i in range(idx, len(arr)):
                if i > idx and arr[i] == arr[i-1]:
                    continue
                if arr[i] > target:
                    break
                sol.append(arr[i])
                self.backtrack(i+1,target-arr[i],arr,res,sol)
                sol.pop()
            
