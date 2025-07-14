# -*- coding: utf-8 -*-

"""
LeetCode Problem: 1385. find-the-distance-value-between-two-arrays
Difficulty: E
Link: https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/description/

Author: VastEpiphany
Date: 2025-07-11

"""

from typing import List

class Solution:
    """
    进行数学公式的变形，|a-b|>d 可变为： a-d < b < a+d,题目要求只要b不出现位于这个区间的元素就没问题
    """
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = 0
        for a in arr1:
            lower = a - d
            upper = a + d

            l_ptr = 0
            r_ptr = len(arr2) - 1

            while l_ptr <= r_ptr:
                mid = (l_ptr+r_ptr) // 2
                if arr2[mid] < lower:
                    l_ptr = mid + 1
                else:
                    r_ptr = mid - 1
            if l_ptr == len(arr2) or arr2[l_ptr] > upper:
                res += 1
        return res

if __name__ == '__main__':  
    sol = Solution()
    print(sol.findTheDistanceValue([4,5,8],[10,9,1,8],2))