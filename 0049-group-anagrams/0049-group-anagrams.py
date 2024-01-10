from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        res = []
        
        for i in strs:
            sorted_s = tuple(sorted(i))
            anagram_map[sorted_s].append(i)
            
        for value in anagram_map.values():
            res.append(value)
        
        return res
            
            
        
        