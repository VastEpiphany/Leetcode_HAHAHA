# -*- encoding: utf-8 -*-
"""
LeetCode Problem: maximal-rectangle
Difficulty: Hard
Tags: Monotonic Stack
Link: https://leetcode.cn/problems/maximal-rectangle/description/
Author: VastEpiphany
Date: 2025-07-24

"""
from typing import List

class Solution:
    '''
    Leetcode 84 Pro Max版  Use a Very smart & tricky way to deal with the problem

    1. 想一下，二维数组计算面积，是否和84题有点像呢？
    2. 重点是问题的一个转化，我们其实可以遍历matrix的每一行，对每一行的每个元素每一列加和后的list使用84的计算方法进行求解
    3. 这样的话我们就能够相当于每一行都进行一次84题的计算了，这样就将二维矩阵的最大面积计算转换为对应84题的求解

    Time Complexicity: O(n^2)
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
    

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        ans = 0
        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        for i in range(n):
            for j in range(m):
                heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0
            ans = max(ans, self.largestRectangleArea(heights))
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(sol.maximalRectangle([["0","1"],["1","0"]]))