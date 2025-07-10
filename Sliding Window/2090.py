# -*- coding: utf-8 -*-

"""
LeetCode Problem: 2090. k-radius-subarray-averages/description
Difficulty: M
Link: https://leetcode.cn/problems/k-radius-subarray-averages/description/

Author: VastEpiphany
Date: 2025-07-10

"""

from typing import List

class Solution:
    '''
    可行但是太菜了，很容易超时

    还是注意滑动窗口的思想，只计算一次sum，然后移动首尾元素（像Queue那样)
    '''
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs = []
        n = len(nums)
    
        for i in range(0,n):
            if i-k < 0 or i+k >= n:
                avgs.append(-1)
                continue
            window_sum = sum(nums[i-k:i+k+1]) # for loop contains a sum loop again O(nk) hard
            avgs.append(window_sum//(2*k+1))
        
        return avgs
    
class Solution1:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        n = len(nums)
        avgs = [-1] * n # A very smart way to init! After all, you know the whole length & the special requirements of -1, so why not just initializing them to -1 at first?
        
        if 2*k+1 > n:
            return avgs
        window_sum = sum(nums[:2*k+1])
        avgs[k] = window_sum // (2*k+1)

        for i in range(2*k+1,n):
            window_sum = window_sum + nums[i] - nums[i-1-2*k]
            avgs[i-k] = window_sum // (2*k+1)
        
        return avgs

if __name__ == "__main__":
    sol = Solution1()
    print(sol.getAverages([7,4,3,9,1,8,5,2,6],3))
    print(sol.getAverages([7],0))
    print(sol.getAverages([7],10000))