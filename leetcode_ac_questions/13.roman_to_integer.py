class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # or use
        nums = [1000, 500, 100, 50, 10, 5, 1]
        roman_char = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        roman_char_and_nums_map = dict(zip(roman_char, nums))

        if len(s) == '' or not s:
            return 0
        elif len(s) == 1:
            return roman_char_and_nums_map.get(s)
        else:
            last, sum = s[0], 0
            for i in range(1, len(s)):
                if roman_char_and_nums_map.get(last) < roman_char_and_nums_map.get(s[i]):
                    sum -= roman_char_and_nums_map.get(last)
                else:
                    sum += roman_char_and_nums_map.get(last)
                last = s[i]
            sum += roman_char_and_nums_map.get(last)
            return sum


s = Solution()
print s.romanToInt('MI')
