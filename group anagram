from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
        results=[ ]
        for s in strs:
            sorted_list=tuple(sorted(s))
            anagrams[sorted_list].append(s)
        for value in anagrams.values():
          results.append(value)
        return results

