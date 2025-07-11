"""
LeetCode Problem: 704. binary-search
Difficulty: E
Link: https://leetcode.cn/problems/binary-search/description/

Author: VastEpiphany
Date: 2025-07-11

"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_ptr = 0
        r_ptr = len(nums)-1

        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            if nums[mid] < target:
                l_ptr = mid + 1
            else:
                r_ptr = mid - 1
        
        if l_ptr >= len(nums):
            return -1
        if nums[l_ptr] != target:
            return -1
        return l_ptr

if __name__ == '__main__':
    sol = Solution()
    print(sol.search([-1,0,3,5,9,12],9))
    print(sol.search([-1,0,3,5,9,12],2))