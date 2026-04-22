class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums); n = len(nums)
        length = 0
        for i in range(n):
            l_0 = 1; j=i
            num = nums[i]
            while (num + 1) in numSet:
                l_0 += 1; num += 1
            length = max(length, l_0)
        return length