class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "" #Creating a new string to traverse the previous string. 
        
        for c in s: #Looping through every element of s.
            if c.isalnum(): #Making sure the element is alphanumerical
                newStr += c.lower() #making the element lower case 
        return newStr == newStr[::-1] 
    
    #Checking if the reverse is equal to our starting string (if true then it     # is palindrome) 
    
    
            