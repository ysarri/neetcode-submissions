class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = start = 0
        for i in range(len(s)-1,-1,-1):
            char = s[i]
            print(char)
            if char == ' ' and start==0:
                continue       
            else:
                start = 1
            if char == ' ':
                break
            length+=1; 
        return length