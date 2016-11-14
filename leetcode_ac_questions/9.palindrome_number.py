class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)

        for i in range(len(x)/2):
            if x[i] != x[len(x) - i - 1]:
                break
        else:
            return True

        return False

s = Solution()
print s.isPalindrome(0)
