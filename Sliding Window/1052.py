# -*- coding: utf-8 -*-

"""
LeetCode Problem: 1052. grumpy-bookstore-owner
Difficulty: M
Link: https://leetcode.cn/problems/grumpy-bookstore-owner/description/

Author: VastEpiphany
Date: 2025-07-11

"""

from typing import List

class Solution:
    '''
    本人的第一个初始解题思路，通过率73/78,在遇到较大的测试集合时会出现超时的问题
    True Essence: Sliding Window while there's 2 list to consider
    key point: "可以让自己连续 minutes 分钟不生气"  continuous window
    '''
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if len(customers) != len(grumpy):
            raise ValueError
        
        ans = 0
        s = 0
        n = len(customers)

        for i in range(n):
            grump_sum = 0

            # Window In
            s += customers[i]

            # At first continue if window len is not enough
            if i - minutes + 1 < 0:
                continue

            # Update Criteria
            # JUDGE：Two For loop，O(n^2) Hard ...TAT...
            zero_index = [j for j in range(n) if (j <(i-minutes+1) or j>i) and grumpy[j] == 0]
            grump_sum = sum(customers[j] for j in zero_index)

            ans = max(ans,s+grump_sum)

            # Window Out
            s -= customers[i-minutes+1]

        return ans
    
    def maxSatisfied1(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        # 计算窗口内 grumpy==1 的顾客数
        add = 0
        max_add = 0
        for i in range(n):
            if grumpy[i] == 1:
                add += customers[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                add -= customers[i - minutes]
            max_add = max(max_add, add)
        return base + max_add


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSatisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3))
    print(sol.maxSatisfied([1],[0],1))