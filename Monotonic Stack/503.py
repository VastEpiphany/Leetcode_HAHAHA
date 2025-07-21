"""
LeetCode Problem: 503. next-greater-element-ii
Difficulty: M
Link: https://leetcode.cn/problems/next-greater-element-ii/description/

Author: VastEpiphany
Date: 2025-07-21

"""
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums) # Notice that the initialization is VERY IMPORTANT in M stack
        stack = []
        n = len(nums)

        for i in range(0,n):
            #i_n = i % n
            i_n = i
            while stack and nums[i_n] > stack[-1]:
                ans[stack.pop()] = nums[i_n]
            
            stack.append(nums[i_n])

if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElements([1,2,1]))