class Solution:
    def reverseWords(self, s: str) -> str:
        s_m = s.split(" ")
        temp = []
        for el in s_m:
            temp.append(el[::-1])
        return " ".join(temp)

obj = Solution()
print(obj.reverseWords("Let's take LeetCode contest"))