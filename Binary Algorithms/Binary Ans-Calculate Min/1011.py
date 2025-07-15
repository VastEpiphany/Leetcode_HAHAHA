# -*- coding: utf-8 -*-

"""
LeetCode Problem: 1011. capacity-to-ship-packages-within-d-days
Difficulty: M
Link: https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/description/

Author: VastEpiphany
Date: 2025-07-14

"""
from typing import List

class Solution:
    '''
    本题目重点是判断条件函数check怎么构思，怎么去写这个是重点
    '''
    def check(self, weights, w, days) -> bool:
        day_count = 1
        cur_sum = 0
        for x in weights:
            if x > w:
                return False  # 单个包裹都装不下
            if cur_sum + x > w:
                '''
                如果当前天再加上包裹 x 超过了运载能力 w，则需要新开一天（day_count += 1），并把当天的重量清零（cur_sum = 0）
                '''
                day_count += 1
                cur_sum = 0
            cur_sum += x
        return day_count <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l_ptr = 1
        r_ptr = sum(weights) # 最大运力是一天运送完所有包裹

        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            if self.check(weights,mid,days):
                r_ptr = mid - 1
            else:
                l_ptr = mid + 1

        return l_ptr

if __name__ == "__main__":
    sol = Solution()
    print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))
    print(sol.shipWithinDays([3,2,2,4,1,4],3))
    print(sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10],1))