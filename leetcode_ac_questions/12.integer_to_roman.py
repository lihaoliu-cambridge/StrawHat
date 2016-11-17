class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str:
        """
        # or use
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_char = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums_and_roman_char_map = dict(zip(nums, roman_char))
        result_list = []
        for k in nums:
            while num >= k and num > 0:
                result_list.append(nums_and_roman_char_map.get(k))
                num -= k

        return ''.join(result_list)

s = Solution()
print s.intToRoman(1)