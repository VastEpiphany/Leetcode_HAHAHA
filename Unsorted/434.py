import re

class Solution:
    def countSegments(self, s: str) -> int:
        splited_words = [word for word in re.split(r'\s+', s.strip()) if word]
        return len(splited_words)

obj = Solution()
print(obj.countSegments("Hello, my name is John"))  # Output: 5
print(obj.countSegments("     "))