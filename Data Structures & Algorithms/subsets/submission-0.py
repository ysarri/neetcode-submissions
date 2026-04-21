class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)

        for i in range(n):
            newL = len(res)
            # res.append([nums[i]])
            for j in range(newL):
                
                new_subset = res[j].copy()
                
                # res_j = [res[j]]
                new_subset.append(nums[i])
                res.append(new_subset)
        return res


