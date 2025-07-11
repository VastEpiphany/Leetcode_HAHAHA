"""
LeetCode Problem: 977. squares-of-a-sorted-array
Difficulty: E
Link: https://leetcode.cn/problems/squares-of-a-sorted-array/description/

Author: VastEpiphany
Date: 2025-07-11

"""
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [x**2 for x in nums]
        l_ptr = 0
        r_ptr = len(nums)

        while l_ptr < r_ptr:
            if nums[l_ptr] > nums[r_ptr]:
                pass
if __name__ == '__main__':
    sol = Solution()
    # print()
    