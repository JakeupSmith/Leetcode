class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {} #using a dictionary to store previously seen numbers 
        
        #num = value, i the index (Enumerate)
        for i, num in enumerate(nums):
            #  9 - 2 = 7
            complement = target - num
            
            #Checking if the value of complement exists in our dictionary 
            # if it does then return the indexs
            if complement in res:
                return [res[complement], i]
        
            #Add the number + index to dictionary {7: 1}
            res[num] = i
        
        return []
            