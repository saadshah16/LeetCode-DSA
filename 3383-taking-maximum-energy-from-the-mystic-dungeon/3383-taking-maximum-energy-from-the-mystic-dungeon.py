class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        max_energy = float('-inf')
        n = len(energy)
        dp = [0] * n

        for i in range(n-1,-1,-1):
            dp[i] =  energy[i] + (dp[i+k] if i + k < n else 0)
            max_energy = max(max_energy, dp[i])
        
        return max_energy

        # TC: O(N)
        # SC: O(N)