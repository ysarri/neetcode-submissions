class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        r = 1
        n = len(nums)
        if n==1:
            return True
        
        p_l = nums[0]%2 # 0 or 1
        while r<n-1:
            p_r = nums[r]%2
            if p_r == p_l:
                return False             
            r+=1; p_l = p_r
        return True
                
