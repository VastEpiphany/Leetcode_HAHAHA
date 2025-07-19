# -*- coding: utf-8 -*-

"""
LeetCode Problem: 1898. maximum-number-of-removable-characters
Difficulty: M
Link: https://leetcode.cn/problems/maximum-number-of-removable-characters/description/

Author: VastEpiphany
Date: 2025-07-16

"""
from typing import List

class Solution:
    '''
    同样是我初步写出来的代码，测试44/67，其实还可以 ^v^ 
    当然剩下的就是run out time问题了，可以看看怎么解决会好一点

    def check(self, s: str, p: str, removable: List[int], k: int) -> bool:
        remove_set = set(removable[:k])
        i = j = 0
        while i < len(s) and j < len(p):
            if i in remove_set:
                i += 1
                continue
            if s[i] == p[j]:
                j += 1
            i += 1
        return j == len(p)
    '''
    def check(self, s: str, p: str, removable: List[int],k: int) -> int:
        # Generate new string that remove the indicated letters
        new_s = ''.join([c for i,c in enumerate(s) if i not in removable[:k]])

        i,j = 0,0
        while i < len(new_s) and j < len(p):
            if new_s[i] == p[j]:
                j += 1
            i += 1
        return True if j == len(p) else False # j == len(p) indicates that p is a subseq of new_s


    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # Binary Search
        l_ptr = 0
        r_ptr = len(removable)

        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            if self.check(s,p,removable,mid):
                l_ptr = mid + 1
            else:
                r_ptr = mid - 1
        
        return r_ptr

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumRemovals("abcacb","ab",[3,1,0]))
    print(sol.maximumRemovals("abcbddddd","abcd",[3,2,1,4,5,6]))
    print(sol.maximumRemovals("abcab","abc",[0,1,2,3,4]))