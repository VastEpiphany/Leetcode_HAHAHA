# -*- encoding: utf-8 -*-
"""
LeetCode Problem: hamming-distance
Difficulty: Easy
Tags: Bit
Link: https://leetcode.cn/problems/hamming-distance/description/
Author: VastEpiphany
Date: 2025-07-25

"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x&~y).count("1") + bin(y&~x).count("1")

if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingDistance(1,4))
    print(sol.hammingDistance(3,1))