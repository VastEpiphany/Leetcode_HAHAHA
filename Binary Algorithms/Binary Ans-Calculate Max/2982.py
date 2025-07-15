# -*- coding: utf-8 -*-

"""
LeetCode Problem: 2982. find-longest-special-substring-that-occurs-thrice-ii
Difficulty: M
Link: https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/description/

Author: VastEpiphany
Date: 2025-07-15

"""
from typing import List
from collections import defaultdict

class Solution:
    '''
    Time Out ... Still very confused and don't want to see it again
    '''
    def check(self,s: str,m: int) -> int:
        dict_cnt = defaultdict(int)

        for i in range(0,len(s)- m + 1):
            dict_cnt[s[i:i+m]] = dict_cnt.get(s[i:i+m],0) + 1
        
        for k in dict_cnt.keys():
            if dict_cnt[k] >= 3 and len(set(k)) == 1: 
                return True
        return False
    
    
    def maximumLength(self, s: str) -> int:
        l_ptr = 1
        r_ptr = len(s) 

        while l_ptr <= r_ptr:
            mid = (l_ptr + r_ptr) // 2
            if self.check(s,mid):
                l_ptr = mid + 1
            else:
                r_ptr = mid - 1
        return r_ptr if r_ptr > 0 else -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumLength("aaaa"))
    #print(sol.maximumLength("aabaabaaba"))
    #print(sol.maximumLength("abcdef")) 
    print(sol.maximumLength("abcaba"))
    #print(sol.maximumLength("ereerrrererrrererre")) # Expected Result: 2
    print(sol.maximumLength("aaaj"))