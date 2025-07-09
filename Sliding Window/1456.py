class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = 0
        ans = 0
        for i,c in enumerate(s):
            if c in 'aeiou':
                vowel += 1
            if i < k-1:
                continue
            ans = max(ans,vowel)

            if s[i-k+1] in 'aeiou':
                vowel -= 1
        return ans
    

a = Solution()
print(a.maxVowels('leetcode',3))