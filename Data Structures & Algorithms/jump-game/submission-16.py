class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        l, r = n - 2, n - 1
        while l>=0:
            # we ask  r - l <= nums[l]?
            if r - l <= nums[l]:
                r = l
                # l goes to the next non-zero nums
                l-=1
                while nums[l]==0:
                    l-=1
            else:
                return False
        return True


    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        l, r = n - 2, n - 1
        while nums[l] == 0 and l > 0:
            l-=1
        while l >= 0:
            # print(l, r)
            if r - l > nums[l]:
                # check that it is also false with the following numbers
                while l>0:   
                    l-=1
                    if r - l <= nums[l]:
                        break
                print(l, r)
                if l == 0 and r - l <= nums[l]: 
                    return True
                if nums[l] == 0 or l == 0:
                    return False
                # if l==0:
                #     return False
            r , l = l, l - 1
            while nums[l] == 0 and l > 0:
                l-=1
        return True