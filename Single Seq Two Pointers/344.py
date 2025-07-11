from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l_ptr = 0
        r_ptr = len(s) - 1
        while l_ptr < r_ptr:
            temp_space = s[l_ptr]
            s[l_ptr] = s[r_ptr]
            s[r_ptr] = temp_space
            l_ptr += 1
            r_ptr -= 1
        return s
    
obj = Solution()
print(obj.reverseString(["H","e","l","l","o"]))