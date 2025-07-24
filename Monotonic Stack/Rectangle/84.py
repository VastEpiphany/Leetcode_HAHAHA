# -*- encoding: utf-8 -*-
"""
LeetCode Problem: largest-rectangle-in-histogram
Difficulty: Hard
Tags: 
Link: https://leetcode.cn/problems/largest-rectangle-in-histogram/description/
Author: VastEpiphany
Date: 2025-07-24

"""
from typing import List

class Solution:
    '''
    我们的目标：
    1. 计算最终的矩形面积公式：r-1-(l+1)-1 = r-l-1
    2. r和l都可以用单调栈求解，当然主要看如何在从左向右遍历height时储存每个元素对应的l和r (maybe list?)
    3. 注意我们维护的是一个单调递增栈，其特点是栈顶元素最大
    '''
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        left = [-1] * n # worst case: the left-most bound of rect is 0
        right = [n] * n # worst case: the right-most bound of rect is n-1
        # stack_l = []
        stack = []

        # calculate the left-most height that smaller than current height
        for i,v in enumerate(heights):
            while stack and v <= heights[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack.clear()
        # calculate the right-most height that smaller than current height
        for i in range(n-1,-1,-1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        for h,l,r in zip(heights,left,right):
            ans = max(ans,h*(r-l-1))

        return ans
                
            

if __name__ == '__main__':
    sol = Solution()
    print(sol.largestRectangleArea([2,1,5,6,2,3]))
    print(sol.largestRectangleArea([2,4]))