# -*- coding: utf-8 -*-

"""
LeetCode Problem: 2226. maximum-candies-allocated-to-k-children
Difficulty: M
Link: https://leetcode.cn/problems/maximum-candies-allocated-to-k-children/description/

Author: VastEpiphany
Date: 2025-07-15

"""
from typing import List

class Solution:
    def check(self,candies: List[int],k: int,m: int) -> bool:
        cnt = 0
        for c in candies:
            cnt += c // m
        return True if cnt >= k else False
    
    def maximumCandies(self, candies: List[int], k: int) -> int:
        '''
        Attention: r_ptr's range can't be min(candies) since the minimum stack of candy can be ignored
        '''
        l_ptr = 1
        r_ptr = sum(candies) // k
        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            if self.check(candies,k,mid):
                l_ptr = mid + 1
            else:
                r_ptr = mid - 1
        
        return r_ptr


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumCandies([5,8,6],3))
    print(sol.maximumCandies([2,5],11))
    print(sol.maximumCandies([1,2,3,4,10],5))
    