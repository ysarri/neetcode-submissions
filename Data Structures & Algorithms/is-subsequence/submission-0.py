class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        for i in range(len(s)):
            if r>=len(t):
                return False
            while r<len(t) and s[i]!=t[r]:
                r+=1
            r+=1
            print(r)
        return True
        


