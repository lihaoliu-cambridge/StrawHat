class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        tmp_head_node = l1
        final_node = tmp_head_node
        tmp_residual = 0
        while (l1 is not None) or (l2 is not None) or (tmp_residual == 1):
            if (tmp_residual == 1) and (l1 is None) and (l2 is None):
                tmp_head_node = ListNode(1)
                break
            tmp_value_1 = 0 if l1 is None else l1.val
            tmp_value_2 = 0 if l2 is None else l2.val
            tmp_sum = tmp_value_1 + tmp_value_2 + tmp_residual
            if tmp_sum >= 10:
                if l1:
                    l1.val = tmp_sum % 10
                if l2:
                    l2.val = tmp_sum % 10
                tmp_residual = 1
            else:
                if l1:
                    l1.val = tmp_sum
                if l2:
                    l2.val = tmp_sum
                tmp_residual = 0
            if l1:
                l1 = l1.next
                tmp_head_node = l1
            if l2:
                l2 = l2.next
                tmp_head_node = l2
        return final_node

