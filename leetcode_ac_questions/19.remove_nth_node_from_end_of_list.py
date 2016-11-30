# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None and n < 1:
            return head

        tmp_node_1, tmp_node_2 = head, head

        for i in range(n):
            if tmp_node_1.next:
                tmp_node_1 = tmp_node_1.next
            else:
                if i == n-1:
                    return head.next
                else:
                    return head

        while tmp_node_1.next:
            tmp_node_1 = tmp_node_1.next
            tmp_node_2 = tmp_node_2.next

        tmp_node_2.next = tmp_node_2.next.next

        return head
