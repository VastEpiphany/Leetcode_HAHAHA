# -*- coding: utf-8 -*-

"""
LeetCode Problem: 2300. successful-pairs-of-spells-and-potions
Difficulty: M
Link: https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/

Author: VastEpiphany
Date: 2025-07-11

"""
from typing import List

class Solution:
    '''
    思路：当然可以暴力O(n^2)进行求解，但是肯定可以更好；注意到成功组合的要求是spell*potion>= success,移项可得
    potion>(success/spell) 然后这个除法是向上取整的，所以我们只要做到将potion进行升序排序，然后找到第一个符合要求的值即可（又转化为binary了）

    时间复杂度 O(nlogn)
    '''
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # The formula below is used to do the up-divide calculation while calculating each spell element's target val
        target = [(success + spells[x]-1) // spells[x] for x in range(len(spells))]

        potions.sort() # First we need to sort the potions list so that we can use the binary search

        res = []

        for i in range(len(target)):
            l_ptr = 0
            r_ptr = len(potions)-1

            while l_ptr <= r_ptr:
                mid = (l_ptr+r_ptr) // 2
                if potions[mid] < target[i]:
                    l_ptr = mid + 1
                else:
                    r_ptr = mid - 1
            
            # Adding some exception handing mechanism
            if l_ptr > len(potions)-1:
                res.append(0)
                continue
            res.append(len(potions)-l_ptr)
        
        return res
        

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.successfulPairs([5,1,3],[1,2,3,4,5],7))
    print(sol.successfulPairs([3,1,2],[8,5,8],16))