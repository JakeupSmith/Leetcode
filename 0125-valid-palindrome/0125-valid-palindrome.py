class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = ""
        
        for i in s:
            if i.isalnum():
                test = test + i
    
        test = test.lower()
        
        t = test[::-1]
        
        for i in range(len(test)):
            if test[i] != t[i]:
                return False
        return True
    
    
            