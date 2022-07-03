class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num = 10001
        maxx = 0
        result = 0
        for p in prices:
            if num > p:
                num = p
            else:
                result = p - num
                if maxx < result:
                    maxx = result
        return maxx