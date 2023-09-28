class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute foce would be O(n)^2 because we could potentially cycle through the list twice. basically check if indx 1 + indx 2 = target. 
        
        res = dict() 
        
        for indx, num in enumerate(nums): #enumerate puts it in the format [0,1] Needed for solution
            if num in res:
                return [res[num], indx]
            else:
                res[target - num] = indx 
            