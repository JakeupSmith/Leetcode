class Solution(object):
    def mergeAlternately(self, word1, word2):
        i, j = 0, 0 

        res = []
        while i < len(word1) and j < len(word2): 
            res.append(word1[i])
            res.append(word2[i])
            i+= 1
            j+= 1
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)