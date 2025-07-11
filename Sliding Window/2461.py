# -*- coding: utf-8 -*-

"""
LeetCode Problem: 2461. maximum-sum-of-distinct-subarrays-with-length-k
Difficulty: M
Link: https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

Author: VastEpiphany
Date: 2025-07-10

"""

from typing import List
from collections import defaultdict

class Solution:
    '''
    Still Not a good solution as you iterate so many times on nums
    '''
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
    
class Solution1:
    '''
    Using Hashing Table (dict in Python) as shown in 2841
    '''
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        s = 0
        hashing_cnt = defaultdict(int)

        for i,n in enumerate(nums):
            s += n
            hashing_cnt[n] += 1

            l = i-k+1
            if l < 0:
                continue

            if len(hashing_cnt) == k:
                res = max(res,s)

            out = nums[l]
            s  -= out
            hashing_cnt[out] -= 1
            if hashing_cnt[out] == 0:
                del hashing_cnt[out] # if no more out elements, just delete this pos
        return res


    
if __name__ == "__main__":
    sol = Solution()
    #print(sol.maximumSubarraySum([1,5,4,2,9,9,9],3))
    print(sol.maximumSubarraySum([4,4,4],3))

    sol1 = Solution1()
    print(sol1.maximumSubarraySum([1,5,4,2,9,9,9],3))
    print(sol1.maximumSubarraySum([4,4,4],3))