# -*- coding: utf-8 -*-

"""
LeetCode Problem: 2576. find-the-maximum-number-of-marked-indices
Difficulty: M
Link: https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/description/

Author: VastEpiphany
Date: 2025-07-15

"""
from typing import List

class Solution:
    '''
    注意题目中所提到的“互不相同”，这点非常重要
    '''
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort() # First to sort the list to ascending order 

        l_ptr = 0
        r_ptr = len(nums) // 2 # since we want to find k pairs so that the total num wouldn't exceed half of that (upper division)

        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            if all(2*nums[i]<=nums[i-mid] for i in range(mid)):
                l_ptr = mid + 1
            else:
                r_ptr = mid - 1
        return r_ptr * 2  # Don't forget that your return is the number of items, not the pairs


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxNumOfMarkedIndices([3,5,2,4]))
    print(sol.maxNumOfMarkedIndices([9,2,5,4]))
    print(sol.maxNumOfMarkedIndices([7,6,8]))