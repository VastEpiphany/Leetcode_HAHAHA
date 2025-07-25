# -*- encoding: utf-8 -*-
"""
LeetCode Problem: number-of-steps-to-reduce-a-number-to-zero
Difficulty: Easy
Tags: Bit
Link: https://leetcode.cn/problems/number-of-steps-to-reduce-a-number-to-zero/description/
Author: VastEpiphany
Date: 2025-07-25

"""

class Solution:
    '''
    时间复杂度 O(1)
    '''
    def numberOfSteps(self, num: int) -> int:
        return bin(num).count('1')*2 + bin(num).count('0') - 2

if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSteps(14))
    print(sol.numberOfSteps(8))
    print(sol.numberOfSteps(123))