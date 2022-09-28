class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum=0
        
        for i in range(len(nums)):
            presum = Counter()
            presum[0] = 1
            sums = 0
            final = 0
            for i in range(len(nums)):
                sums += nums[i]
                final += presum[sums - k]
                presum[sums] += 1
            return final