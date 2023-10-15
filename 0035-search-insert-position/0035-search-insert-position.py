class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Log(n)
        
        l, r = 0, len(nums) -1  #initiating and -1 so we don't go over the index. (binary search)
        
        while l <= r:  
            mid = (l + r) // 2
            
            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                l = mid + 1
                
            else:
                r = mid - 1
                
        return l