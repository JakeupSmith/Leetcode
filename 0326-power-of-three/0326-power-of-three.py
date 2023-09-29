class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:    #Anything less than 0 will be false 
            return False 
        
        x, i = 1,0  
        
        while x <= n:  #Bacially goes until it reaches a value of a power of three. 
            if x == n: 
                return True
            i+=1 
            x = 3**i
        return False