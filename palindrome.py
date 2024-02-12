class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reversed_num=0
        temp=x
        while temp!=0:
            rem=temp%10
            reversed_num=reversed_num*10+rem
            temp//=10
        return reversed_num==x

