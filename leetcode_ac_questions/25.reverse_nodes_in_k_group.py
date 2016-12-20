# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node_pre, node_now, node_last, last_turn_last_node, reversed_head = None, head, head, None, None

        while node_last:
            for i in range(k):
                if node_last:
                    node_last = node_last.next
                else:
                    break
            else:
                node_tmp_start, node_tmp_end = node_now, None

                while node_now != node_last:
                    if node_now.next == node_last:
                        node_tmp_end = node_now

                    node_next = node_now.next
                    node_now.next = node_pre

                    node_pre = node_now
                    node_now = node_next

                if not reversed_head:
                    reversed_head = node_tmp_end

                node_tmp_start.next = node_now
                node_pre = node_tmp_start

                if last_turn_last_node:
                    last_turn_last_node.next = node_tmp_end
                last_turn_last_node = node_tmp_start

        if reversed_head:
            return reversed_head
        else:
            return head


a = ListNode(1)
a.next = ListNode(2)
b = ListNode(3)
b.next = ListNode(4)
a.next.next = b
b.next.next = ListNode(5)
b.next.next.next = ListNode(6)
s = Solution()
c = s.reverseKGroup(a, 4)
while c:
    print c.val
    c = c.next
