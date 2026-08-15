class Solution(object):
    def isPalindrome(self,x):

        s=str(x)
        return s==s[::-1]

sol=Solution()
print(sol.isPalindrome(121))
