class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        latest_position_for_char = {}
        start, end, max_length = 0, 0, 0
        for i in range(len(s)):
            if s[i] in latest_position_for_char:
                if start <= latest_position_for_char.get(s[i]):
                    start = latest_position_for_char.get(s[i]) + 1
                end += 1
                latest_position_for_char[s[i]] = i
            else:
                end += 1
                latest_position_for_char.setdefault(s[i], i)

            cur_length = end - start
            if max_length < cur_length:
                max_length = cur_length

        return max_length
