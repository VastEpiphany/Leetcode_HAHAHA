# -*- coding: utf-8 -*-

"""
LeetCode Problem: 475. heaters
Difficulty: M
Link: https://leetcode.cn/problems/heaters/description/

Author: VastEpiphany
Date: 2025-07-15

"""
from typing import List

class Solution:
    """
    其实重点还是这个check函数可以怎么去写  我们的思路是：
    1. 对于当前给定的半径 r，遍历每个房子，判断是否都能被加热到。
    2. 对于每个房子 house，我们用指针 j 找到第一个位置在 house - r 及以后的 heater（即能覆盖 house 左侧的最左 heater）。
    3. 如果所有 heater 都在 house - r 左侧（j == len(heaters)），说明 house 无法被任何 heater 覆盖，返回 False。
    4. 否则，检查当前 heater[j] 到 house 的距离是否超过 r，如果超过，说明 house 也无法被加热，返回 False。
    5. 如果所有 house 都能被加热，返回 True。
    """
    def check(self,houses,heaters,r):
        """
        Priori Condition: houses / heaters MUST BE SORTED !!!
        """
        j = 0 # current index for our heaters
        for house in houses:
            while j < len(heaters) and heaters[j] < house - r:
                j += 1
            if j == len(heaters) or abs(heaters[j]-house)> r:
                return False
        return True
    
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        l_ptr = 0 # Actually 0 is possible if all house's position is contained in heater's list
        # Our Upper bound might be a little bit tricky, it should be the case that for each of the house, we shall compare
        # it with the farthest heaters (i.e. heaters[0]/[-1]) and find the max distance
        r_ptr = max(
            max(abs(house-heaters[0]) for house in houses),
            max(abs(house-heaters[-1]) for house in houses)
        )

        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            if self.check(houses,heaters,mid):
                r_ptr = mid - 1
            else:
                l_ptr = mid + 1
        return l_ptr

if __name__ == '__main__':
    sol = Solution()
    print(sol.findRadius([1,2,3],[2]))
    print(sol.findRadius([1,2,3,4],[1,4]))
    print(sol.findRadius([1,5],[10]))