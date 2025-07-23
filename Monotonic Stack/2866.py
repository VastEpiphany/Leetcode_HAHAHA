# -*- encoding: utf-8 -*-
"""
LeetCode Problem: 2866. beautiful-towers-ii
Difficulty: M
Tags: Monotonic Stack
Link: https://leetcode.cn/problems/beautiful-towers-ii/description/
Author: VastEpiphany
Date: 2025-07-23

"""
from typing import List

class Solution:
    '''
    思路可以，值得赞赏，但是仍有问题，就是说step1的考虑是错误的，你不能
    '''
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        ans = sum(maxHeights) # 本人认为初始化应该是这样做的
        stack_r = []
        stack_l = []

        # Step 1: 无论如何我们总要找到对应最大位置的元素作为“山峰”
        p_i = maxHeights.index(max(maxHeights))

        # Step 2: 不知道能否对两边分别用不同的遍历方式进行单调栈的维护 (对山峰右侧进行单调栈处理)
        for e in maxHeights[p_i:]:
            while stack_r and e <= stack_r[-1]:
                stack_r.pop()
            if stack_r and e > stack_r[-1]:
                ans -= (e - stack_r[-1])
            stack_r.append(e)

        # Step 3: 对山峰左侧进行单调栈处理
        for e in reversed(maxHeights[:p_i+1]):
            while stack_l and e <= stack_l[-1]:
                stack_l.pop()
            if stack_l and e > stack_l[-1]:
                ans -= (e - stack_l[-1])
                continue
            stack_l.append(e)

        return ans

class BetterSolution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        
        # 计算每个位置作为峰值时，左侧的最大和
        left = [0] * n
        stack = []  # 存储索引
        for i in range(n):
            # 维护单调递增栈
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            if stack:
                # 当前位置的贡献 = 前一个有效位置的和 + 当前高度 * 区间长度
                left[i] = left[stack[-1]] + maxHeights[i] * (i - stack[-1])
            else:
                # 栈为空，说明前面所有位置都可以用当前高度
                left[i] = maxHeights[i] * (i + 1)
            stack.append(i)
        
        # 计算每个位置作为峰值时，右侧的最大和
        right = [0] * n
        stack = []  # 存储索引
        for i in range(n - 1, -1, -1):
            # 维护单调递增栈
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            if stack:
                # 当前位置的贡献 = 后一个有效位置的和 + 当前高度 * 区间长度
                right[i] = right[stack[-1]] + maxHeights[i] * (stack[-1] - i)
            else:
                # 栈为空，说明后面所有位置都可以用当前高度
                right[i] = maxHeights[i] * (n - i)
            stack.append(i)
        
        # 计算最大总和
        max_sum = 0
        for i in range(n):
            # left[i] + right[i] - maxHeights[i] (因为峰值被计算了两次)
            max_sum = max(max_sum, left[i] + right[i] - maxHeights[i])
        
        return max_sum
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumSumOfHeights([5,3,4,1,1]))
    print(sol.maximumSumOfHeights([6,5,3,9,2,7]))
    print(sol.maximumSumOfHeights([3,2,5,5,2,3]))