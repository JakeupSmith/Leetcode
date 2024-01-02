class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums = sorted(nums)
        
        # 1,1,1,2,3,3,4
        #Checking in the iteration if the res list already contains the element given. 
        for i in nums:
            found = False
            for j in res:
                if i not in j:
                    j.append(i)
                    found = True
                    break
            if not found:
                res.append([i])
            
        return res