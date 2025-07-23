"""
LeetCode Problem: 3113. find-the-number-of-subarrays-where-boundary-elements-are-maximum
Difficulty: H
Link: https://leetcode.cn/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/description/

Author: VastEpiphany
Date: 2025-07-23

"""
from typing import List
import math

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        '''
        注意我们的subarray 需要两个相同的元素相连，并不是说中间可以有隔开的这样
        
        思路：
        1. 首先将我们的答案初始化为list中元素个数（这个是至少可以保证的）
        2. ⭐ 我们的栈结构是可以有微调的，我们可以用嵌套list[0]位置来记录元素值，[1]作为我们的counter进行计数
        3. 我们做一个底大顶小的stack，然后将无用的元素pop掉（要理解这个pop是怎么一回事）
        4. 如果和前面栈顶元素相等，证明我们找到了一个相邻且符合的，ans加一，然后统计数据也加一
        '''
        ans = len(nums) # 因为每一个单独的元素都能组成一个符合要求的子数组，所以这样初始化
        stack = [[math.inf,0]]

        for i in range(len(nums)):
            while stack and nums[i] > stack[-1][0]:
                stack.pop()
            if nums[i] == stack[-1][0]:
                ans += stack[-1][1]
                stack[-1][1] += 1
            else:
                stack.append([nums[i],1])

        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSubarrays([1,4,3,3,2]))
    print(sol.numberOfSubarrays([3,3,3,3]))