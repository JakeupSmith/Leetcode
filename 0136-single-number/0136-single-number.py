class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for i in nums:
            res = i ^ res #if the number isn't the same as the previous. + 1 
        return res
            