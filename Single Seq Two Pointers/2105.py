# -*- coding: utf-8 -*-

"""
LeetCode Problem: 2105. watering-plants-ii
Difficulty: M
Link: https://leetcode.cn/problems/watering-plants-ii/description/

Author: VastEpiphany
Date: 2025-07-11

"""

from typing import List

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        A_ptr = 0
        B_ptr = len(plants) - 1
        A_left = capacityA
        B_left = capacityB
        A_cnt, B_cnt = 0, 0
        
        while A_ptr < B_ptr:
            # Alice
            if plants[A_ptr] <= A_left:
                A_left -= plants[A_ptr]
            else:
                A_cnt += 1
                A_left = capacityA - plants[A_ptr]
            # Bob
            if plants[B_ptr] <= B_left:
                B_left -= plants[B_ptr]
            else:
                B_cnt += 1
                B_left = capacityB - plants[B_ptr]
            A_ptr += 1
            B_ptr -= 1

        if A_ptr == B_ptr:
            # 谁剩的多谁来浇
            if A_left >= B_left:
                if plants[A_ptr] > A_left:
                    A_cnt += 1
                # 不管需不需要refill，最后都要浇掉这棵
                # A_left = max(A_left - plants[A_ptr], 0) # 可省略
            else:
                if plants[B_ptr] > B_left:
                    B_cnt += 1
                # B_left = max(B_left - plants[B_ptr], 0) # 可省略

        return A_cnt + B_cnt
        


if __name__ == "__main__":
    sol = Solution()
    #print(sol.minimumRefill([2,2,3,3],5,5))
    print(sol.minimumRefill([1,2,4,4,5],6,5))