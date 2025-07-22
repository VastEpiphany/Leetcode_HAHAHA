"""
LeetCode Problem: 853. car-fleet
Difficulty: M
Link: https://leetcode.cn/problems/car-fleet/

Author: VastEpiphany
Date: 2025-07-21

"""
from typing import List

class Solution:
    '''
    Treat this problem as a chasing problem. We don't care about where the two car would confront with each other
    What we care is that if the two car satisfy the condition, it means that the latter would spend less time than the previous car

    Hence:
    1. sort the pos in ascending order
    2. calculate each car's time to the target
    3. tranverse, for each of the car, if any latter car's time is less than current one, then it's a fleet
    '''
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = [0] * n
        stack = []

        # Notice that both the order of the pos/speed !
        for i,(pos,spd) in enumerate(sorted(zip(position,speed))):
            time[i] = (target - pos) / spd
        
        for v in time:
            while stack and v >= stack[-1]:
                stack.pop()
            stack.append(v)
        return len(stack)

if __name__ == '__main__':
    sol = Solution()
    print(sol.carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))
    print(sol.carFleet(10,[3],[3]))
    print(sol.carFleet(100,[0,2,4],[4,2,1]))