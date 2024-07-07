class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        TotalBottles = 0
        empty = 0
        while numBottles > 0:
            TotalBottles += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange

        return TotalBottles
        
