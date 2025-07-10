# -*- coding: utf-8 -*-

"""
LeetCode Problem: 2841. maximum-sum-of-almost-unique-subarray
Difficulty: M
Link: https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/

Author: VastEpiphany
Date: 2025-07-10

"""

from typing import List

class Solution:
    """
    属于sliding window的思想，但不算最快的（很慢），因为每次都要新建一个set，时间复杂度O(nk)
    Solution: Hashing table (dict) 维护窗口内每个元素出现次数
    """
    def aus_judge(self,l,m):
        s = set(l)
        return True if len(s) >= m else False

    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        index = 0
        for i in range(k-1,n):
            if self.aus_judge(nums[i-k+1:i+1],m):
                aus_sum = sum(nums[i-k+1:i+1])
                index = i
                break
            if i == n-1 and self.aus_judge(nums[i-k+1:i+1],m) == False:
                return 0
        max_sum = aus_sum

        for i in range(index+1,n):
            aus_sum = aus_sum + nums[i] - nums[i-k]
            if self.aus_judge(nums[i-k+1:i+1],m):
                max_sum = max(aus_sum,max_sum)
        
        return max_sum



if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSum([2,6,7,3,1,7],3,4))
    print(sol.maxSum([5,9,9,2,4,5,4],1,3))
    print(sol.maxSum([1,2,1,2,1,2,1],3,3))

    print(sol.maxSum([2,1,1,4],2,2))