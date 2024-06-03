class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        
        while left <= right:
            mid = (left+right)//2
            mid_square = mid*mid
            
            if mid_square == num:
                return True
            elif mid_square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
    # TC: O(log n)
    # SC: O(1)