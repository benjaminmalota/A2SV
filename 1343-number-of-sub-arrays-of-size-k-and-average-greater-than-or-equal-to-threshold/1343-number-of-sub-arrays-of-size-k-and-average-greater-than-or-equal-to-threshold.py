class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        n = len(arr)
        sums = sum(arr[:k])
        res = sums
        stack = []
        if sums/k >= threshold:
            stack.append(sums)
            
        for r in range(len(arr)-k):
            res = res - arr[r]+arr[r+k]
            if res/k >= threshold:
                stack.append(res)
            l+1
        return len(stack)
            
        
        
            
            
        