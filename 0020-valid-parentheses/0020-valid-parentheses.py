class Solution:
    def isValid(self, s) -> bool:
        stack = []
        
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                #only appending the opening brackets 
                stack.append(char)
            elif char in dict.keys():
                #If the stack is empty or the ], }, ) != [, {, (
                if stack == [] or dict[char] != stack.pop():
                    return False
        return stack == []
                    
                    
            
            