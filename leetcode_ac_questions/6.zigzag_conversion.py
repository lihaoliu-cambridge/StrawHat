class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0 or numRows < 2:
            return s

        reset_s = []

        for i in range(numRows):
            j = i

            while j <= len(s) - 1:
                reset_s.append(s[j])

                if i != 0 and i != numRows - 1:
                    k = j + 2 * (numRows - i - 1)
                    if k < len(s):
                        reset_s.append(s[k])

                j += 2 * numRows - 2

        return ''.join(reset_s)

s = Solution()
print s.convert("PAYPALISHIRING", 3)
