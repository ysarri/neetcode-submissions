class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newInt = 1; n = len(digits)
        for i,dig in enumerate(digits):
            newInt += 10**(n-i-1)*dig
        return [int(d) for d in str(newInt)]
        