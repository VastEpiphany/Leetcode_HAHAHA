# -*- encoding: utf-8 -*-
"""
LeetCode Problem: maximum-score-of-a-good-subarray
Difficulty: Hard
Tags: 
Link: https://leetcode.cn/problems/maximum-score-of-a-good-subarray/description/
Author: VastEpiphany
Date: 2025-07-24

"""
from typing import List

class Solution:
    """
    本题目是84题的升级版，建议搭配一起食用

    想一下，我们84题实际上就是求解这样一个矩形的面积，只不过这个题目要求我们的矩形必须包含下标k，那就加上判断条件即可
    """
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        left = [-1] * n # worst case: the left-most bound of rect is 0
        right = [n] * n # worst case: the right-most bound of rect is n-1
        # stack_l = []
        stack = []

        # calculate the left-most height that smaller than current height
        for i,v in enumerate(nums):
            while stack and v <= nums[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack.clear()
        # calculate the right-most height that smaller than current height
        for i in range(n-1,-1,-1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        for h,l,r in zip(nums,left,right):
            # THE ONLY THING THAT IS DIFFERENT FROM THE LEETCODE PROBLEM 84 !!
            if l < k < r:
                ans = max(ans,h*(r-l-1))

        return ans
    
    def maximumScore2(self, nums: List[int], k: int) -> int:
        '''
        注意到我们本题目其实还可以使用双指针的方法进行求解
        '''
        ans = 0
        l_ptr, r_ptr = k, k
        min_val = nums[k]
        n = len(nums)
        while l_ptr > 0 or r_ptr < n - 1:
            # 优先扩展较大的一侧
            left_val = nums[l_ptr - 1] if l_ptr > 0 else float('-inf')
            right_val = nums[r_ptr + 1] if r_ptr < n - 1 else float('-inf')
            if left_val > right_val:
                l_ptr -= 1
                min_val = min(min_val, nums[l_ptr])
            else:
                r_ptr += 1
                min_val = min(min_val, nums[r_ptr])
            ans = max(ans, min_val * (r_ptr - l_ptr + 1))
        # 还要考虑只包含 k 的情况
        ans = max(ans, nums[k])
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumScore2([1,4,3,7,4,5],3))