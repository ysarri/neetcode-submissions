class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s)==0:
            return t

        countS = {}; n = len(t)
        countT = {}
        for i in range(n):
            countT[t[i]] = 1 + countT.get(t[i],0)
            if i == n-1:
                break    
            countS[s[i]] = 1 + countS.get(s[i],0)


        for c in t:
            if c not in countS or countT[c]>countS[c]:
                return c

