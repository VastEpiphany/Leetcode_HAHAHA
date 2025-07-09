from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        Hmm... Does solve the problem, but not good enough. costs too much
        '''
        ans = float('-inf')
        avg = 0
        sum = 0
        for i,c in enumerate(nums):
            # Special Cases
            if k == 1:
                return max(nums)
            # To skip just a few items
            if i < k-1 :
                sum += c
                avg = sum / (i+1)
                continue
            
            # If not, then do the 2rd step, move a block forward
            avg = (avg*(k-1) + c) / k
            ans = max(ans,avg)

            avg = (avg*k - nums[i-k+1]) / (k-1)

        return ans
    
class BetterSolution:
    '''
     记住Sliding Window的实质是滑动，计算avg也是这样，不用想太麻烦，计算avg的分母太麻烦就可以拿掉也无所谓的
    '''
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k,len(nums)):
            window_sum = window_sum + nums[i] - nums[i-k]
            max_sum = max(window_sum,max_sum)

        return max_sum / k
    

a = Solution()
print(a.findMaxAverage([1,12,-5,-6,50,3],4))
print(a.findMaxAverage([5],1))


b = BetterSolution()
print(b.findMaxAverage([1,12,-5,-6,50,3],4))
print(b.findMaxAverage([5],1))
            