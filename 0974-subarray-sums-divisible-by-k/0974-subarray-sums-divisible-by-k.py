class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        m, tot = [1] + [0 for i in range(k - 1)], 0
        
        for i in accumulate(nums):
            tot += m[i%k]
            m[i%k] += 1
        
        return tot