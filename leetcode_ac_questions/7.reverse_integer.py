class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed_x = int(str(abs(x))[::-1])

        if x < 0:
            reversed_x *= -1

        if reversed_x > 2 ** 31 or reversed_x < -1 * (2 ** 31 - 1):
            return 0
        else:
            return reversed_x


s = Solution()
print s.reverse(1534236469)
