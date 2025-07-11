import re
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pattern = "|".join(wordDict)
        words = re.findall(pattern,s)

        return words
    
obj = Solution()
print(obj.wordBreak("catscatsandog",["cats", "dog", "sand", "and", "cat"]))