# -*- coding: utf-8 -*-

"""
LeetCode Problem: 275. h-index-ii
Difficulty: M
Link: https://leetcode.cn/problems/h-index-ii/description/

Author: VastEpiphany
Date: 2025-07-15

"""
from typing import List

class Solution:
    '''
    判定条件和左右边界都比较简单，当然这个是练习闭区间求最大值的初始题目所以不会很难，需要注意我们判断条件和返回指针同求最小值的不一致性在哪里
    '''
    def check(self,citations,m):
        return True if citations[-m] >= m else False

    def hIndex(self, citations: List[int]) -> int:
        l_ptr = 0
        r_ptr = len(citations)

        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            if self.check(citations,mid):
                l_ptr = mid + 1
            else:
                r_ptr = mid - 1
        return r_ptr


if __name__ == "__main__":
    sol = Solution()
    print(sol.hIndex([0,1,3,5,6]))
    print(sol.hIndex([1,2,100]))