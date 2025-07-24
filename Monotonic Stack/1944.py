# -*- encoding: utf-8 -*-
"""
LeetCode Problem: 1944. number-of-visible-people-in-a-queue
Difficulty: Easy/Medium/Hard
Tags: Monotonic Stack
Link: https://leetcode.cn/problems/number-of-visible-people-in-a-queue/description/
Author: VastEpiphany
Date: 2025-07-23

"""
from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        stack = []

        for i in range(n-1,-1,-1):
            while stack and heights[i] > stack[-1]:
                stack.pop()
                ans[i] += 1
            if stack:
                ans[i] += 1
            stack.append(heights[i])

        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.canSeePersonsCount([10,6,8,5,11,9]))