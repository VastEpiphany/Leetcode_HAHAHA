# -*- coding: utf-8 -*-

"""
LeetCode Problem: 1283. find-the-smallest-divisor-given-a-threshold
Difficulty: M
Link: https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/description/

Author: VastEpiphany
Date: 2025-07-14

"""
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        '''
        本题我们采用两端都是闭区间的解法（这样的话l/r需要分别初始化为1和max(nums)-1 均可以取到）

        e.g. nums=[1,2,5,9]  threshold=6
             -> 在[1,2,3,4,5,6] 中寻找符合要求的最小的m （最小问题，可以转化为二分）
             -> Judgment Criteria: \sigma 下取整(num[i]-1/m) + n <= threshold
        '''
        n = len(nums)
        l_ptr,r_ptr = 1,max(nums)-1

        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            # 等价于 ceil(x/mid)
            if sum((x-1)//mid for x in nums) <= threshold - n:
                r_ptr = mid- 1
            else:
                l_ptr = mid + 1
        
        return l_ptr

if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestDivisor([1,2,5,9],6))