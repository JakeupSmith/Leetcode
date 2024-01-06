class Solution:
    def search(self, nums: List[int], target: int) -> int:
            res = -1 
            
            for i, num in enumerate(nums):
                if num == target:
                    res = i
            return res