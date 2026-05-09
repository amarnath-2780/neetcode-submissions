class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            mark = tuple(sorted(word))
            if mark not in group:
                group[mark] = []
                
            group[mark].append(word)
        
        return list(group.values())