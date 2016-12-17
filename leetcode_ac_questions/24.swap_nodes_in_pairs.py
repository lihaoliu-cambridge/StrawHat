# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_pre, node_now, node_next = ListNode(0), head, None
        if node_now and node_now.next:
            node_next = node_now.next
        else:
            return head

        head = node_pre

        while node_now and node_next:
            node_now.next = node_next.next
            node_next.next = node_now
            node_pre.next = node_next

            node_pre = node_now
            node_now = node_now.next
            node_next = node_now.next if node_now else None

        return head.next

a = ListNode(1)
a.next = ListNode(2)
b = ListNode(3)
b.next = ListNode(4)
a.next.next = b
s = Solution()
c = s.swapPairs(a)
while c:
    print c.val
    c = c.next
