# -*- coding: utf-8 -*-

"""
LeetCode Problem: 2461. maximum-sum-of-distinct-subarrays-with-length-k
Difficulty: M
Link: https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

Author: VastEpiphany
Date: 2025-07-10

"""

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        index = 0
        for i in range(k-1,n):
            if len(set(nums[i-k+1:i+1])) == k:
                mssum = sum(nums[i-k+1:i+1])
                max_sum = mssum
                index = i
                break
            if i == n-1 and set(nums[i-k+1:i+1]) != k:
                return 0
        
        for i in range(index+1,n):
            mssum = mssum + nums[i] - nums[i-k]
            if len(set(nums[i-k+1:i+1])) == k:
                max_sum = max(max_sum,mssum)
        return max_sum
    
if __name__ == "__main__":
    sol = Solution()
    #print(sol.maximumSubarraySum([1,5,4,2,9,9,9],3))
    print(sol.maximumSubarraySum([4,4,4],3))