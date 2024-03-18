regular expression matching


PYTHON SOLUTION
PYTHON SOLUTION
456
VIEWS
0
Last Edit: August 22, 2022 2:45 PM

yamdaminda
yamdaminda
 33
Runtime: 56 ms, faster than 84.11% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 14.2 MB, less than 27.97% of Python3 online submissions for Regular Expression Matching.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def rec(s_index, p_index):
            if (s_index, p_index) in cache: 
                return cache[(s_index, p_index)]
            
            if s_index >= len(s) and p_index >= len(p): 
                cache[(s_index, p_index)] = True
                return cache[(s_index, p_index)]
            
            if p_index >= len(p): 
                cache[(s_index, p_index)] = False
                return cache[(s_index, p_index)]
            
            match = (s_index < len(s) and p[p_index] in {s[s_index], '.'} )
            
            if p_index + 1 <len(p) and p[p_index +1] == '*':                
                cache[s_index, p_index] = rec(s_index, p_index + 2) or (match and rec(s_index + 1, p_index))               
                return cache[s_index, p_index]
            
            if match:
                cache[s_index, p_index] = rec(s_index + 1, p_index+1)
                return cache[s_index, p_index]
            
            cache[s_index, p_index] = False
            return cache[s_index, p_index]
        
        return rec(0, 0)
