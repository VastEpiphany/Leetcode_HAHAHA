# -*- encoding: utf-8 -*-
"""
LeetCode Problem: binary-gap
Difficulty: Easy
Tags: Bit
Link: https://leetcode.cn/problems/binary-gap/description/
Author: VastEpiphany
Date: 2025-07-25

"""

class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        last = -1
        for i in range(n.bit_length()):
            if (n >> i) & 1:
                if last != -1:
                    ans = max(ans, i - last)
                last = i
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.binaryGap(22))
    