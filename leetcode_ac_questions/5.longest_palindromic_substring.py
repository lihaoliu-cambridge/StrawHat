class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list('#' + '#'.join(list(s)) + '#')
        s_len = len(s_list)
        max_mid_pos = 0
        max_substring_length = 0
        substring_length_list = [0] * s_len

        for no, c in enumerate(s_list):
            if no < max_mid_pos + max_substring_length:
                substring_length_list[no] = min(substring_length_list[2 * max_mid_pos - no],
                                                max_mid_pos + max_substring_length - no)
            else:
                substring_length_list[no] = 1

            while no + substring_length_list[no] < s_len and 0 <= no - substring_length_list[no] and \
                            s_list[no - substring_length_list[no]] == s_list[no + substring_length_list[no]]:
                substring_length_list[no] += 1

            if substring_length_list[no] >= max_substring_length:
                max_substring_length = substring_length_list[no]
                max_mid_pos = no

        return_list = s_list[max_mid_pos - max_substring_length + 1: max_mid_pos + max_substring_length]
        longest_palindromic_substring = filter(lambda char: char != '#', return_list)
        return ''.join(longest_palindromic_substring)


s = Solution()
print s.longestPalindrome("1")
