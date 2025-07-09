from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
        l = []
        for w in words:
            for i in range(3):
                if all(c in r[i] for c in w.upper()):
                    l.append(w)
                    break
        return l

# Test cases
obj = Solution()
print(obj.findWords(["Hello", "Alaska", "Dad", "Peace"]))  # Expected output: ["Alaska", "Dad"]
