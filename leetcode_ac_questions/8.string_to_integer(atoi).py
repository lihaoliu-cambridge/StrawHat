class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str is None or str == '':
            return 0

        result_int = 0
        positive_sign = True

        if str[0] == '-':
            positive_sign = False
        elif str[0] == '+':
            pass
        elif str[0].isdigit():
            result_int = result_int * 10 + int(str[0])
        else:
            return 0

        for c in str[1: len(str)]:
            if not c.isdigit():
                break
            else:
                result_int = result_int * 10 + int(c)

        if not positive_sign:
            result_int *= -1

        if result_int > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif result_int < -1 * 2 ** 31:
            return -1 * 2 ** 31

        return result_int


s = Solution()
print s.myAtoi('2147483648')
