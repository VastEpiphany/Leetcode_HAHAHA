# -*- coding: utf-8 -*-

"""
LeetCode Problem: 2379. minimum-recolors-to-get-k-consecutive-black-blocks
Difficulty: E
Link: https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/

Author: VastEpiphany
Date: 2025-07-10

"""

from typing import List

class Solution:
    '''
    Exactly the same way, if you discover the truth under the problem
    1. Calculate each sub-seq's num of B, and find the seq that contains the max num of B
    2. Answer: K-MAX(B)  Then problem solved~
    '''
    def minimumRecolors(self, blocks: str, k: int) -> int:
        B_num = blocks[:k].count('B')
        max_B_num = B_num

        for i in range(k,len(blocks)):
            in_flag = 1 if blocks[i] == 'B' else 0
            out_flag = 1 if blocks[i-k] == 'B' else 0
            B_num = B_num + in_flag - out_flag

            max_B_num = max(B_num,max_B_num)

        return k - max_B_num

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumRecolors("WBBWWBBWBW",7))
    print(sol.minimumRecolors("WBWBBBW",2))