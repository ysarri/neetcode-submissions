class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1

        # for i in n:
        while r>l:
            # m = l + (r-l)//2
            add = numbers[l] + numbers[r]
            if add > target:
                r -= 1
            #     r = m - 1
            elif add < target:
                 l += 1
            else:
                return [l + 1, r + 1]
        

