"""
LeetCode Problem: 35. search-insert-position
Difficulty: E
Link: https://leetcode.cn/problems/search-insert-position/description/

Author: VastEpiphany
Date: 2025-07-11

"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l_ptr = 0
        r_ptr = len(nums)-1

        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            if nums[mid] < target:
                l_ptr = mid + 1
            else:
                r_ptr = mid - 1

        return l_ptr

if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1,3,5,6],5))
    print(sol.searchInsert([1,3,5,6],2))
    print(sol.searchInsert([1,3,5,6],7))