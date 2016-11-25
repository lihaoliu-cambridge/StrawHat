class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_and_char_mapping = {'0': [''],
                                  '1': [''],
                                  '2': ['a', 'b', 'c'],
                                  '3': ['d', 'e', 'f'],
                                  '4': ['g', 'h', 'i'],
                                  '5': ['j', 'k', 'l'],
                                  '6': ['m', 'n', 'o'],
                                  '7': ['p', 'q', 'r', 's'],
                                  '8': ['t', 'u', 'v'],
                                  '9': ['w', 'x', 'y', 'z']}
        all_results = []
        self.getLetterCombinations(all_results, digit_and_char_mapping, digits, 0)
        return all_results

    def getLetterCombinations(self, all_results, digit_and_char_mapping, digits, position, iter_list=None):
        if not iter_list:
            iter_list = []

        if len(iter_list) == len(str(digits)):
            iter_str = ''.join(iter_list)
            if iter_str and iter_str is not '':
                all_results.append(iter_str)

        try:
            digit = str(digits)[position]
            for i in digit_and_char_mapping.get(digit):
                iter_list.append(i)
                self.getLetterCombinations(all_results, digit_and_char_mapping, digits, position + 1, iter_list)
                iter_list.pop()
        except IndexError:
            return None


s = Solution()
print s.letterCombinations('123456')
