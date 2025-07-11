import re

class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        parts = re.split(r'/', longUrl)
        unencode = parts[-1]
        temp = []
        
        return unencode
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        pass

obj = Codec()
print(obj.encode("https://leetcode.com/problems/design-tinyurl"))