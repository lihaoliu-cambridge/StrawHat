class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result_list = []
        self.get_seq(n, n, result_list)
        return result_list

    def get_seq(self, left, right, result_list, string_list=None):
        if string_list is None:
            string_list = []

        if left == 0 and right == 0:
            result_list.append(''.join(string_list))
        else:
            if left > 0:
                string_list.append('(')
                self.get_seq(left - 1, right, result_list, string_list)
                string_list.pop()
            if left < right:
                string_list.append(')')
                self.get_seq(left, right - 1, result_list, string_list)
                string_list.pop()


s = Solution()
print s.generateParenthesis(5)
