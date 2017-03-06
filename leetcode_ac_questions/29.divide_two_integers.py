class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if divisor == 0:
            return 2 ** 31 - 1

        positive_flag = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)

        times = 0
        while dividend >= (divisor << 1):
            divisor <<= 1
            times += 1

        ret = 0
        while times >= 0:
            if dividend >= divisor:
                dividend -= divisor
                ret += 1 << times
            divisor >>= 1
            times -= 1

        ret *= positive_flag
        if ret >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif ret <= -1 * 2 ** 31:
            return -1 * 2 ** 31
        else:
            return ret


s = Solution()
print s.divide(-2147483648, 1)

