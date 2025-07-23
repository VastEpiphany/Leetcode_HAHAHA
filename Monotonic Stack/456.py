"""
LeetCode Problem: 456. 132-pattern
Difficulty: M
Link: https://leetcode.cn/problems/132-pattern/description/

Author: VastEpiphany
Date: 2025-07-23

"""
from typing import List

class Solution:
    '''
    本题难度还是很大的 TVT  
    
    '''
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        n_min = float('-inf')

        for i in range(len(nums)-1,-1,-1):
            if nums[i] < n_min:
                return True
            while stack and nums[i] > stack[-1]:
                n_min = stack.pop()

            stack.append(nums[i])
        return False

                    
            

if __name__ == '__main__':
    sol = Solution()
    print(sol.find132pattern([-1,3,2,0]))