# -*- coding: utf-8 -*-

"""
LeetCode Problem: 1343. 大小为K且平均值大于等于阈值的子数组数目求解
Difficulty: M
Link: https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold

Author: VastEpiphany
Date: 2025-07-10

Problem Summary:
给你一个整数数组 arr 和两个整数 k 和 threshold 。

请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。

Approach:
输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)
"""

from typing import List

# Thinking: Easy task as long as you use slide window, just noticing that how to transfer
#           threshold to sum terms
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum_thres = threshold * k 
        thres_counter = 0
        window_sum = sum(arr[:k])
        #res = window_sum
        if window_sum >= sum_thres:
            thres_counter += 1 

        for i in range(k,len(arr)):
            window_sum = window_sum + arr[i] - arr[i-k]
            #res = max(res,window_sum)
            if window_sum >= sum_thres:
                thres_counter += 1
        return thres_counter

if __name__ == "__main__":
    sol = Solution()
    print(sol.numOfSubarrays([11,13,17,23,29,31,7,5,2,3],3,5))