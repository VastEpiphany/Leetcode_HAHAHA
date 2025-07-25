# -*- encoding: utf-8 -*-
"""
LeetCode Problem: power-of-two/four
Difficulty: Easy
Tags: 
Link: https://leetcode.cn/problems/power-of-two/description/
Author: VastEpiphany
Date: 2025-07-26

"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False # 不要忘了special case！
        return True if bin(n).count('1') == 1 else False
    
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 or bin(n).count('1') != 1:
            return False
        
        for i in range(n.bit_length()):
            if (n >> i)& 1 and i % 2 == 0:
                return True
            else:
                continue
        return False
    def isPowerOfFourOptimize(self, n: int) -> bool:
        # n > 0 
        # (n & (n - 1)) == 0 n只有一个1（2的幂）
        # 这个1出现在偶数位（从0开始），即 n & 0xAAAAAAAA == 0（0xAAAAAAAA是所有奇数位为1的掩码）
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0
    

if __name__ == '__main__':
    sol = Solution()
    #print(sol.isPowerOfTwo(1))
    #print(sol.isPowerOfTwo(16))
    #print(sol.isPowerOfTwo(3))
    print(sol.isPowerOfFour(-3))