class Solution(object):
    def isPalindrome(self, s):
        left=0
        t=len(s)
        right=t-1
        while left < right:
            if not s[left].isalnum(): 
                left=left+1
            elif not s[right].isalnum() :
                right=right-1
            elif s[left].lower()!=s[right].lower():
                 return False
            else:
                left=left+1
                right=right-1
        return True

            
