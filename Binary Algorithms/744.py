"""
LeetCode Problem: 744. find-smallest-letter-greater-than-target
Difficulty: E
Link: https://leetcode.cn/problems/find-smallest-letter-greater-than-target/description/

Author: VastEpiphany
Date: 2025-07-11

"""
from typing import List

class Solution:
    '''
    Key Point: Python Ord function transferring alphabet to ASCII numbers
    '''
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l_ord = [ord(x) for x in letters]

        l_ptr = 0
        r_ptr = len(l_ord)-1

        while l_ptr <= r_ptr:
            mid = (l_ptr+r_ptr) // 2
            if l_ord[mid] <= ord(target):
                l_ptr = mid + 1
            else:
                r_ptr = mid - 1

        if l_ptr >= len(l_ord):
            return letters[0]
        
        return letters[l_ptr]

if __name__ == '__main__':
    sol = Solution()
    #print(sol.nextGreatestLetter(["c","f","j"],"a"))
    print(sol.nextGreatestLetter(["c","f","j"],"c"))
