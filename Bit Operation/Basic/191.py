# -*- encoding: utf-8 -*-
"""
LeetCode Problem: number-of-1-bits
Difficulty: Easy
Tags: Bit
Link: https://leetcode.cn/problems/number-of-1-bits/description/
Author: VastEpiphany
Date: 2025-07-26

"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n>0:
            s = n // 2
            l = n % 2

            if l == 1:
                cnt += 1
            n = s

        return cnt            

    def hammingWeight1(self, n: int) -> int:
        return bin(n).count('1')


if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingWeight(11))
    print(sol.hammingWeight(128))
    print(sol.hammingWeight(2147483645))