class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g stands for children? s stands for cookies
        
        # basically checking if the values are equal if they are then res += 1
        g = sorted(g)
        s = sorted(s)
        
        
        res = 0
        i, j = 0, 0
        
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                res += 1
                i += 1
            j += 1
        
        return res