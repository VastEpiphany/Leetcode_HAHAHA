# -*- coding: utf-8 -*-

"""
LeetCode Problem: 1423. maximum-points-you-can-obtain-from-cards
Difficulty: M
Link: https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/description/

Author: VastEpiphany
Date: 2025-07-11

"""

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        r_num = n - k  # IMPORTANT: Actually what you want is a continuous sub-list, so just think in the opposite way, why not choosing the rest of the sub-list 
        s_min = 0
        ans = float('inf')

        if k == n:
            return sum(cardPoints)

        for i,x in enumerate(cardPoints):
            # ENTER THE WINDOW
            s_min += x

            if i - r_num + 1 < 0: # WHEN THE SIZE OF THE WINDOW IS NOT ENOUGH
                continue

            # UPDATE THE ANS
            ans = min(ans,s_min)

            # REMOVE THE LAST NUM OF THE WINDOW
            s_min -= cardPoints[i-r_num+1]

        return total_sum-ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxScore([1,2,3,4,5,6,1],3))
    print(sol.maxScore([9,7,7,9,7,7,9],7))