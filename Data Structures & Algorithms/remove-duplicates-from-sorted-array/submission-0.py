class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = 0
        seen = []
        for i in range(len(nums)):
            n1 = nums[i] 
            if n1 not in seen:
                seen.append(n1)
                nums[last] = nums[i]
                last+=1
            print(nums, last)
            # else:
            # else:
        return last