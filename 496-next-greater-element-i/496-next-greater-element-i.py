class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index1 = {n:i for i, n in enumerate(nums1)}
        ans = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            x = nums2[i]
            while stack and x > stack[-1]:
                popped = stack.pop()
                index = index1[popped]
                ans[index] = x
            if x in index1:
                stack.append(x)
                
        return ans
                