class Solution:

    def binary_search(self,nums,targ,l,r):
        while l<=r:
            m = l + (r-l)//2
            print(l,m,r)
            if nums[m]>targ:
                r=m-1
            elif nums[m]<targ:
                l=m+1
            else:
                return m
        return -1

    def search(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        l,r = 0, n-1

        return self.binary_search(nums, target, l, r)


