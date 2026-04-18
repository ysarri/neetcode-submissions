class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k=0
        for i in range(n):         
            nums[k]=nums[i]; 
            if nums[k]==val:
                continue
            k+=1
        return k
            