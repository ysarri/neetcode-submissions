class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxL=0
        tmpL=0
        for dig in nums:
            if dig==1:
                tmpL+=1
                maxL = max(tmpL,maxL)
            else:
                tmpL = 0
        return maxL


