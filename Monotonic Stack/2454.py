# -*- encoding: utf-8 -*-
"""
LeetCode 2454. next-greater-element-iv
Difficulty: Hard
Tags: Monotonic Stack
Link: https://leetcode.cn/problems/next-greater-element-iv/description/
Author: VastEpiphany
Date: 2025-07-24

"""
from typing import List

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        stack_l = []

        for i in range(n):
            while stack_l and nums[i] > nums[stack_l[-1]]:
                ans[stack_l.pop()] = nums[i]
                
            m = len(stack) - 1
            while m >= 0  and nums[i] > nums[stack[m]]:
                m -= 1
            stack_l += stack[m+1:] # 直接把整个一段元素都移动到我们另外一个stack中
            del stack[m+1:] # 然后进行手动删除pop （这里我们故意这样循环进行操作，其实也可以正常进行pop，但那样就嵌套while了时间复杂度太高）
            stack.append(i)
        
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.secondGreaterElement([2,4,0,9,6]))