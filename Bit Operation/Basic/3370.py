# -*- encoding: utf-8 -*-
"""
LeetCode Problem: smallest-number-with-all-set-bits
Difficulty: Easy
Tags: Bit
Link: https://leetcode.cn/problems/smallest-number-with-all-set-bits/description/
Author: VastEpiphany
Date: 2025-07-25

"""

class Solution:
    def smallestNumber(self, n: int) -> int:
        return 2**n.bit_length() - 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestNumber(5))
    print(sol.smallestNumber(10))
    