# -*- encoding: utf-8 -*-
"""
LeetCode Problem: find-the-k-or-of-an-array
Difficulty: Easy
Tags: Bit
Link: https://leetcode.cn/problems/find-the-k-or-of-an-array/
Author: VastEpiphany
Date: 2025-07-25

"""
from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = []
        for i in range(max(x.bit_length() for x in nums)): # 我们这样选取最长的元素进行遍历
            cur_bit = [(s>>i)&1 for s in nums]
            ans.append(1) if cur_bit.count(1) >= k else ans.append(0)
        
        if not ans:  # 注意处理当输入全为0时的情况
            return 0
        binary_str = ''.join(str(b) for b in ans[::-1])
        return int(binary_str,2)
                


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKOr([7,12,9,8,9,15],4))
    print(sol.findKOr([2,12,1,11,4,5],6))
    print(sol.findKOr([0],1))