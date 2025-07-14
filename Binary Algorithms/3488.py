# -*- coding: utf-8 -*-

"""
LeetCode Problem: 3488. closest-equal-element-queries
Difficulty: M
Link: https://leetcode.cn/problems/closest-equal-element-queries/description/

Author: VastEpiphany
Date: 2025-07-12

"""
import bisect
from typing import List
from collections import defaultdict

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = [-1] * len(queries)
        # Generate a hashing table that contains each value's position list
        pos = defaultdict(list)
        n = len(nums)
        for i,x in enumerate(nums):
            pos[x].append(i) # Noticing that we just instantiated the val type to list in the default dict
        
        #q_v = [nums[q] for q in queries]

        for l in pos.values():
            if len(l) == 1:
                continue
            # Add the cycling elements as it's a circle list
            l.insert(0,l[-1]-n)
            l.append(l[1] + n)
        # Your target: In each list of the nums[q], you shall find the only element of q and then do the calculation
        # Which is---> Binary Search Algo!
        for i, q in enumerate(queries):
            val = nums[q]
            arr = pos[val]

            if len(arr) <= 3:  # 原始只出现一次（只插入了2个补点+1个原始点）
                ans[i] = -1
                continue

            l_ptr = bisect.bisect_left(arr, q)

            d1 = float('inf') if l_ptr - 1 < 0 else abs(q - arr[l_ptr - 1])
            d2 = float('inf') if l_ptr + 1 >= len(arr) else abs(q - arr[l_ptr + 1])
            ans[i] = min(d1, d2)

        return ans

if __name__ == '__main__':
    sol = Solution()

    #print(sol.solveQueries([1,3,1,4,1,3,2],[0,3,5]))
    print(sol.solveQueries([2,10,20,20,20],[1,4,2]))
    