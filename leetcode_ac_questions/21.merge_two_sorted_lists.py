# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp_start_node = ListNode(0)
        tmp_head_node = tmp_start_node

        while l1 or l2:
            if l1 and not l2:
                while l1:
                    tmp_start_node.next = l1
                    tmp_start_node = tmp_start_node.next
                    l1 = l1.next
            elif not l1 and l2:
                while l2:
                    tmp_start_node.next = l2
                    tmp_start_node = tmp_start_node.next
                    l2 = l2.next
            else:
                if l1.val <= l2.val:
                    tmp_start_node.next = l1
                    tmp_start_node = tmp_start_node.next
                    l1 = l1.next
                else:
                    tmp_start_node.next = l2
                    tmp_start_node = tmp_start_node.next
                    l2 = l2.next

        return tmp_head_node.next
