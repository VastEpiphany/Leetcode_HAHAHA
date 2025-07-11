"""
LeetCode Problem: 34. find-first-and-last-position-of-element-in-sorted-array
Difficulty: M
Link: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Author: VastEpiphany
Date: 2025-07-11

"""
from typing import List


class Solution:
    '''
    记住二分法的几个关键问题：
    1. 区间的开闭（确定mid值后如何更新l/r ptr的位置？是闭区间还是左开右闭这样？）
    2. 循环终止的条件？（R<L 但是是否有附加的情况处理？比如ptr越界怎么办）

    时间复杂度 O(logn)
    '''
    def find_lower_bound(self,nums,target):
        l_ptr = 0
        r_ptr = len(nums)-1

        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            if nums[mid] < target:
                l_ptr = mid + 1
            elif nums[mid] >= target:
                r_ptr = mid - 1
        return l_ptr

    def find_upper_bound(self,nums,target):
        l_ptr = 0
        r_ptr = len(nums)-1

        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            if nums[mid] <= target:
                l_ptr = mid + 1
            elif nums[mid] > target:
                r_ptr = mid - 1
        return r_ptr


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l_index = self.find_lower_bound(nums,target)
        # 3 cases that indicates failure:
        # a. empty list []
        # b. l ptr goes beyond range
        # c. normally returns ptr (satisy r<l) but the corresponding value isn't the target (which indicates there's no target val)
        if len(nums) == 0 or l_index >= len(nums) or nums[l_index] != target:
            return [-1,-1]
        r_index = self.find_upper_bound(nums,target)

        return [l_index,r_index]



if __name__ == '__main__':
    sol = Solution()
    #print(sol.searchRange([5,7,7,8,8,10],8))
    #print(sol.searchRange([5,7,7,8,8,10],6))
    #print(sol.searchRange([],0))
    print(sol.searchRange([2,2],3))