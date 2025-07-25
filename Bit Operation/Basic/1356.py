# -*- encoding: utf-8 -*-
"""
LeetCode Problem: sort-integers-by-the-number-of-1-bits
Difficulty: Easy
Tags: Bit
Link: https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/description/
Author: VastEpiphany
Date: 2025-07-25

"""
from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        '''
        我们针对arr中每个元素采用基于key的lambda匿名函数进行sort，sort的顺序是首先根据其二进制数中所包含的1的个数，如果一样，则采用下一个判断规则，即x本身大小
        '''
        ans = sorted(arr,key=lambda x:(bin(x).count("1"),x))
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortByBits([0,1,2,3,4,5,6,7,8]))
    #sol.sortByBits([0,1,2,3,4,5,6,7,8])