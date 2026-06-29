class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        y =x
        rev = 0

        while y>0:
            lastno=y%10
            rev = (rev*10)+lastno
            y=y//10
        
        return x == rev