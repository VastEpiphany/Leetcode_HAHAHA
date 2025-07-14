# -*- coding: utf-8 -*-

"""
LeetCode Problem: 2070. most-beautiful-item-for-each-query
Difficulty: M
Link: https://leetcode.cn/problems/most-beautiful-item-for-each-query/description/

Author: VastEpiphany
Date: 2025-07-13

"""
from typing import List
import bisect

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda item:item[0]) # # lambda无名函数根据price大小排序
        for i in range(1,len(items)):
            items[i][1] = max(items[i-1][1],items[i][1])
        for i,q in enumerate(queries):
            ind = bisect.bisect_right(items,q,key=lambda item:item[0])
            queries[i] = items[ind-1][1] if ind else 0
        return queries

if __name__ == "__main__":
    sol = Solution()
    #print()