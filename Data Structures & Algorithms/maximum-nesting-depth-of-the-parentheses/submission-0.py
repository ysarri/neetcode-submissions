class Solution:
    def maxDepth(self, s: str) -> int:
        # stack = []
        count = res = 0
        for c in s:
            if c=="(":
                # stack.append("(")
                count+=1
                res = max(count, res)
            if c==")":
                # stack.pop()
                count-=1
        return res