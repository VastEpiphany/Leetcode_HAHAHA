# -*- encoding: utf-8 -*-
"""
LeetCode Problem: Problem Title
Difficulty: Easy
Tags: Bit
Link: https://leetcode.cn/problems/number-complement/
Author: VastEpiphany
Date: 2025-07-25

"""

class Solution:
    def findComplement(self, num: int) -> int:
        mask = (1 << num.bit_length()) - 1
        complement = mask ^ num
        return complement
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.findComplement(5))