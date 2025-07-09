from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        ans,avg = 0
        sum = 0
        for i,c in enumerate(nums):
            if i < k-1 :
                sum += c
                avg = sum / (i+1)
        return ans
            