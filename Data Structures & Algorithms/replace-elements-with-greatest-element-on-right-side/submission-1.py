class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmpM = maxR = arr[-1]
        arr[-1]=-1; k = len(arr)-2
        while k>0:
            tmpM = arr[k]
            arr[k] = maxR
            maxR = max(tmpM,maxR)
            k-=1
        if len(arr)>1:
            arr[0]=maxR
        return arr