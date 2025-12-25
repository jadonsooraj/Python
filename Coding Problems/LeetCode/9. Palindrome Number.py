# M-1: Brute Force
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        ls=[]
        num=x
        while num > 0:
            ls.append(num % 10)
            num=num//10
        ls_rev=ls[::-1]
        if ls == ls_rev:
            return True
        else:
            return False
        
# M-2: Optimise:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev_half=0
        while x > rev_half:
            rev_half = rev_half*10 + x%10
            x = x//10
        
        return x == rev_half or x == rev_half//10