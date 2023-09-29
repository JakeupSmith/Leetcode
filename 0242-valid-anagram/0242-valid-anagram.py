class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #Hashmap Solution
        
        if len(s) != len(t):  #if they aren't equal lengths return false.
            return False
        
        countS, countT = {}, {} #creating two lists. 
        
        
        for i in range(len(s)): #We know they are equal lengths so go through the string. 
            countS[s[i]] = 1 + countS.get(s[i], 0) #Going through s string, every charcter gets added to 1. 
            countT[t[i]] = 1 + countT.get(t[i], 0) #Going through t string, every character gets added to 1. Default = 0 
        for c in countS: #Go through the hashmaps and see if the counts are equal and if they aren't true, then false
            if countS[c] != countT.get(c, 0):
                return False 
            
        return True  #if not false then it must be true. 
        
        