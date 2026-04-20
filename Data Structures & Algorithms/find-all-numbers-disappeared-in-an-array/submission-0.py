class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)

        res = []
        for num in range(1,len(nums)+1):
            if num not in count:
                res.append(num)
        return res       


