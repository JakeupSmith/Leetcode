class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = "" #This also completes edge case. 

        for i in range(len(strs[0])): #Taking two loops that go through. 
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]: #Checking if 1st string = 2nd string. 
                    return res        
            res += strs[0][i]
            
        return res