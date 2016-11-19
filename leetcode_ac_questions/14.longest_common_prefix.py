class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == [] or not strs:
            return ''

        longest_common_prefix = reduce(self.get_longest_common_prefix_between_two_strs, strs)

        return longest_common_prefix

    def get_longest_common_prefix_between_two_strs(self, x, y):
        len_x, len_y = len(x), len(y)

        if len_x == 0 or len_x == 0 or not x or not y:
            return ''

        search_length = len_x if len_x < len_y else len_y

        prefix_length = search_length
        for i in range(search_length):
            if x[i] != y[i]:
                prefix_length = i
                break

        return x[:prefix_length]

s = Solution()
print s.longestCommonPrefix(['abcd', 'ab', 'abb', 'abcdefg'])
