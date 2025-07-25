# -*- encoding: utf-8 -*-
"""
LeetCode Problem: number-of-bit-changes-to-make-two-integers-equal
Difficulty: Easy
Tags: Bit
Link: https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/description/
Author: VastEpiphany
Date: 2025-07-25

"""

class Solution:
    def minChanges(self, n: int, k: int) -> int:
        return bin(n&~k).count("1") if k&n == k and k | n == n else -1

if __name__ == '__main__':
    sol = Solution()

    # n = 0b1101
    # k = 0b0100

    # print(bin(k&n),bin(k|n)) # bin(k&n) == k  且  bin(k|n) == n，说明为子集

    print(sol.minChanges(13,4))
    print(sol.minChanges(21,21))
    print(sol.minChanges(14,13))