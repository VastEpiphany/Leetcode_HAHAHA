# -*- encoding: utf-8 -*-
"""
LeetCode Problem: find-the-prefix-common-array-of-two-arrays
Difficulty: Medium
Tags: Bit
Link: https://leetcode.cn/problems/find-the-prefix-common-array-of-two-arrays/description/
Author: VastEpiphany
Date: 2025-07-25

"""
from typing import List

class Solution:
    def findThePrefixCommonArray1(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        c = [0] * n
        for i in range(n):
            mask_A,mask_B = 0,0
            for x in A[:i+1]:
                mask_A |= 1 << x
            for x in B[:i+1]:
                mask_B |= 1 << x
            
            c[i] = bin(mask_A & mask_B).count('1')
        return c
    
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        c = [0] * n
        mask_A, mask_B = 0, 0
        for i in range(n):
            mask_A |= 1 << A[i]
            mask_B |= 1 << B[i]
            c[i] = bin(mask_A & mask_B).count('1')
        return c
            


if __name__ == '__main__':
    sol = Solution()
    print(sol.findThePrefixCommonArray([1,3,2,4],[3,1,2,4]))
    print(sol.findThePrefixCommonArray([2,3,1],[3,1,2]))