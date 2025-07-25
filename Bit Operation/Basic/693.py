# -*- encoding: utf-8 -*-
"""
LeetCode Problem: binary-number-with-alternating-bits
Difficulty: Easy
Tags: Bit
Link: https://leetcode.cn/problems/binary-number-with-alternating-bits/description/
Author: VastEpiphany
Date: 2025-07-25

"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        flag = None
        for i in range(n.bit_length()):
            if flag == None:
                flag = (n >> i) & 1
            else:
                if flag != (n >> i) & 1:
                    flag = not flag
                else:
                    return False
        return True
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.hasAlternatingBits(5))
    print(sol.hasAlternatingBits(7))
    print(sol.hasAlternatingBits(11))
    print(sol.hasAlternatingBits(6))