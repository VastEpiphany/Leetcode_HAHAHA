"""
LeetCode Problem: 1475. final-prices-with-a-special-discount-in-a-shop
Difficulty: E (M if non-violence)
Link: https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop

Author: VastEpiphany
Date: 2025-07-20

"""

from typing import List

class Solution:
    '''
    Time Complexicity: O(N)
    '''
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices

        for i,v in enumerate(prices):
            while stack and v <= prices[stack[-1]]:
                ans[stack[-1]] -= v
                stack.pop()
            
            stack.append(i)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.finalPrices([8,4,6,2,3]))
    print(sol.finalPrices([1,2,3,4,5]))
    print(sol.finalPrices([10,1,1,6]))