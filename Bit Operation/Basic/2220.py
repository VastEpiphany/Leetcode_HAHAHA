# -*- encoding: utf-8 -*-
"""
LeetCode Problem: minimum-bit-flips-to-convert-number
Difficulty: Easy
Tags: Bit
Link: https://leetcode.cn/problems/minimum-bit-flips-to-convert-number/
Author: VastEpiphany
Date: 2025-07-25

"""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start&~goal).count('1') + bin(goal&~start).count('1')

if __name__ == '__main__':
    sol = Solution()
    print(sol.minBitFlips(10,7))