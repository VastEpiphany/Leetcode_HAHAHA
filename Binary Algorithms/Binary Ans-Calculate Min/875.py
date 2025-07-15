# -*- coding: utf-8 -*-

"""
LeetCode Problem: 875. koko-eating-bananas
Difficulty: M
Link: https://leetcode.cn/problems/koko-eating-bananas/description/

Author: VastEpiphany
Date: 2025-07-14
"""

from typing import List

class Solution:
    '''
    def check(self,piles,h,k) -> bool:
        cur_hour = 0
        cur_ind = 0
        p = piles
        rest_sum = sum(p)

        while cur_hour <= h and cur_ind <= len(p)-1:
            if p[cur_ind] <= k:
                cur_hour += 1
                rest_sum -= p[cur_ind]
                cur_ind += 1
            else:
                cur_hour += 1
                rest_sum -= k
                p[cur_ind] -= k
        
        return True if rest_sum <= 0 else False
    '''
    
    def check(self, piles, h, k) -> bool:
        # 不修改原始piles，直接计算总小时数
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k  # 等价于math.ceil(pile/k)
        return hours <= h
    

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Step 1: Determine the Binary search boundaries (open/close inteval? the max upper boundary?)
        l_ptr = 1
        r_ptr = max(piles) # Max Upper Bound Speed: Eat a whole pile at 1 single hour (ok since we ensure that len(piles)<=h)

        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            if self.check(piles,h,mid):
                r_ptr = mid - 1
            else:
                l_ptr = mid + 1
        return l_ptr

if __name__ == "__main__":
    sol =  Solution()
    print(sol.check([3,6,7,11],8,3))
    print(sol.minEatingSpeed([3,6,7,11],8))