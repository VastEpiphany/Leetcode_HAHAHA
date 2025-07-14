# -*- coding: utf-8 -*-

"""
LeetCode Problem: 2187. minimum-time-to-complete-trips
Difficulty: M
Link: https://leetcode.cn/problems/minimum-time-to-complete-trips/description/

Author: VastEpiphany
Date: 2025-07-14

"""
from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # 首先定义好我们的二分法查找答案的区间
        l_ptr = 1
        r_ptr = max(time) * totalTrips # 最大不可能超过这个数值

        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            if sum(mid // t for t in time) >= totalTrips:
                r_ptr = mid - 1
            else:
                l_ptr = mid + 1
        
        return l_ptr


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTime([1,2,3],5))
    