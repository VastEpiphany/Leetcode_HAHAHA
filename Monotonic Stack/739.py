# -*- coding: utf-8 -*-

"""
LeetCode Problem: 739. daily-temperatures
Difficulty: M
Link: https://leetcode.cn/problems/daily-temperatures/description/

Author: VastEpiphany
Date: 2025-07-19

"""

from typing import List

class Solution:
    '''
    因为是第一次在python中表示stack结构，要注意一些细节：
    1. Python 中的stack采用list表示，并且单独有pop函数代表移除栈顶元素
    2. list左侧代表栈底元素，右侧代表栈顶元素
    3. 注意到stack的结构是后进先出

    结果：通过了，但是代码还可以再进行优化
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # initialize new empty stack
        ans = [0] * len(temperatures)
        stack.append([len(temperatures)-1,temperatures[-1]])

        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[i] >= stack[-1][1]: # Only need to consider the top element of the stack, which is the stack[-1]
                stack.pop()
            if stack:
                ans[i] = stack[-1][0] - i
            stack.append([i,temperatures[i]])

        return ans
    
class BetterSolution:
    '''
    1. 考虑一下我们的stack可以存什么，不一定是ind和val都存吧？ 所以可以只存index
    2. stack中对应的温度应该是从左向右递减的（bottom->top）
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i,v in enumerate(temperatures):
            while stack and v > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return ans



if __name__ == '__main__':
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))

    sol1 = BetterSolution()
    print(sol1.dailyTemperatures([73,74,75,71,69,72,76,73]))