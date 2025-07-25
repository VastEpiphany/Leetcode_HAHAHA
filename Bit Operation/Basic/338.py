# -*- encoding: utf-8 -*-
"""
LeetCode Problem: Problem Title
Difficulty: Easy/Medium/Hard
Tags: Array/String/Linked List/Tree/Graph/DP/Backtracking
Link: 
Author: VastEpiphany
Date: 2025-07-26

"""
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)

        for i in range(1,n+1):
            ans[i] = bin(i).count('1')
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countBits(2))
    print(sol.countBits(5))