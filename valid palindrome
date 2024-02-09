class Solution:
    def isPalindrome(self, s: str) -> bool:
        st, end = 0, len(s)-1
        while st<=end:
            if not s[st].isalnum():
                st+=1
            elif not s[end].isalnum():
                end-=1
            elif s[st].lower()!=s[end].lower():
                return False
            else:
                st+=1
                end-=1
        
        
        return True
        
