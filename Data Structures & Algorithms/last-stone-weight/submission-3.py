class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1: return stones[0]
        stones.sort();
        while stones[-2]>0:
            print(stones)
            x, y = stones[n - 2], stones[n - 1]
            if x == y:
                stones[n - 1], stones[n - 2] = 0, 0
                # i+=2
            elif x < y:
                diff = y - x
                stones[n - 1], stones[n - 2] = 0, diff
            stones.sort();
        return stones[-1]


