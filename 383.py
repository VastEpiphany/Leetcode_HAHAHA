class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1 = {}

        for ch in ransomNote:
            freq1[ch] = freq1.get(ch,0) + 1
        
        for ch in magazine:
            if ch in freq1:
                freq1[ch] -= 1
        
        for count in freq1.values():
            if count > 0:
                return False
        return True
        


obj = Solution()
print(obj.canConstruct("aa","aab"))
print(obj.canConstruct("aa","ab"))