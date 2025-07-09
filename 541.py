class Solution:
    '''
    采用分组的思想去进行解决
    '''
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)
        n = len(l)
        
        for i in range(0,n,2*k):
            end = min(n,i+k) # 如果i+k小，证明还没到最后一组或者最后一组数量小于k
            l[i:end] = l[i:end][::-1]
        return ''.join(l)
    
obj = Solution()
print(obj.reverseStr("abcdefg",3))