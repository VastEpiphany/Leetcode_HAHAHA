import re

class Solution:
    def reverseWords(self, s: str) -> str:
        word = re.split(r'\s+',s.strip())
        
        l_ptr = 0
        r_ptr = len(word) - 1
        while l_ptr < r_ptr:
            word[l_ptr],word[r_ptr] = word[r_ptr],word[l_ptr]
            l_ptr += 1
            r_ptr -= 1
        result = " ".join(word)
        return result
    

obj = Solution()
print(obj.reverseWords("a good   example"))