"""
LeetCode Problem: 503. next-greater-element-ii
Difficulty: M
Link: https://leetcode.cn/problems/next-greater-element-ii/description/

Author: VastEpiphany
Date: 2025-07-21

"""
from typing import List

class Solution:
    '''
    Time Complexicity: O(n)
    '''
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums) # Notice that the initialization is VERY IMPORTANT in M stack
        stack = []
        n = len(nums)

        for i in range(0,2 * n):
            i_n = i % n
            while stack and nums[i_n] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i_n]
            
            # 所谓的循环数组，就是说我们的求解范围变了，所以我们需要对应加入入栈条件
            if i < n:
                stack.append(i_n)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElements([1,2,1]))