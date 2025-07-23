"""
LeetCode Problem: 456. 132-pattern
Difficulty: M
Link: https://leetcode.cn/problems/132-pattern/description/

Author: VastEpiphany
Date: 2025-07-23

"""
from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        n_min = float('inf')

        for i in range(len(nums)-3,1,-1):
            if nums[i] < n_min:
                n_min = nums[i]
            while stack and nums[i+1] >= stack[-1]:
                stack.pop()
            stack.append(nums[i+1])
            

if __name__ == '__main__':
    sol = Solution()
    # print

    stack = []
    nums = [3,9,5,7,4,2,0]
    for i in range(len(nums)-1,-1,-1):
        while stack and nums[i] > stack[-1]:
            stack.pop()
        stack.append(nums[i])
    print(stack[-1])