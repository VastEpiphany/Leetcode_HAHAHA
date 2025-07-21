"""
LeetCode Problem: 496. next-greater-element-i
Difficulty: E
Link: https://leetcode.cn/problems/next-greater-element-i/description/

Author: VastEpiphany
Date: 2025-07-20

"""
from typing import List

class Solution:
    '''
    Time Complexicity:O(n+m)
    '''
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      ans = [-1] * len(nums1)
      stack = []
      idx = {v:i for i,v in enumerate(nums1)}

      for v in nums2:
         while stack and v > stack[-1]:
            ans[idx[stack.pop()]] = v
         if v in idx:
            stack.append(v)
      return ans
if __name__ == "__main__":
   sol = Solution()
   print(sol.nextGreaterElement([4,1,2],[1,3,4,2]))