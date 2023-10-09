class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" } #Creating a hashmap from the closing to the opening so(). 

        for c in s:                    
            if c in closeToOpen:        #Checking if it is within closeToOpen if it is then it is a closing paraenthesis. 
                if stack and stack[-1] == closeToOpen[c]: #Checking if they match one another. 
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(c) #appending in case we get ((( start. 
            
        return True if not stack else False