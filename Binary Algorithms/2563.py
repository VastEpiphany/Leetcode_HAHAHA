# -*- coding: utf-8 -*-

"""
LeetCode Problem: 2563. count-the-number-of-fair-pairs
Difficulty: M
Link: https://leetcode.cn/problems/count-the-number-of-fair-pairs/

Author: VastEpiphany
Date: 2025-07-13

"""

from typing import List
import bisect

class Solution:
    '''
    Initial Thinking: We shall just sort the nums into ascending order so that we can 
    tranverse the lowest value nums[i], using bisect to find the number of indicated nums[j]
    
    Formula:  lower - nums[i] <= nums[j] <= upper - nums[i]

    BUT NOT GOOD ENOUGH AS you slice nums and bisect them every time in the for loop
    '''
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort() # 原地排序
        n = len(nums)
        ans = 0

        for i,e in enumerate(nums):
            big_arr = nums[i+1:]
            l = lower - e
            u = upper - e

            left = bisect.bisect_left(big_arr,l)
            right = bisect.bisect_right(big_arr,u)

            ans += (right-left)

        return ans
    
    def countFairPairs1(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort() # 原地排序
        n = len(nums)
        ans = 0

        for i,e in enumerate(nums):
            l = lower - e
            u = upper - e

            left = bisect.bisect_left(nums,l,i+1,n)
            right = bisect.bisect_right(nums,u,i+1,n)

            ans += (right-left)

        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.countFairPairs([0,1,7,4,4,5],3,6))
    print(sol.countFairPairs([1,7,9,2,5],11,11))