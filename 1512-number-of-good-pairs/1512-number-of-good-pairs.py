class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        index = {}
        res = 0
        
        for i in nums:
            if i in index:
                res += index[i]
                index[i] += 1
            else:
                index[i] = 1
        return res