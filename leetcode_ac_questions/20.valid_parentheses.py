class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        fake_stack = []
        for i in s:
            if i not in ['(', ')', '[', ']', '{', '}']:
                return False

            fake_stack.append(i)

            try:
                if fake_stack[-2] + fake_stack[-1] in ['()', '[]', '{}']:
                    fake_stack.pop()
                    fake_stack.pop()
            except IndexError as e:
                pass

        if len(fake_stack) == 0:
            return True
        else:
            return False


s = Solution()
print s.isValid('()')

