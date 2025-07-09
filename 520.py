class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Check if all letters are uppercase or all letters are lowercase or only the first letter is uppercase
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())