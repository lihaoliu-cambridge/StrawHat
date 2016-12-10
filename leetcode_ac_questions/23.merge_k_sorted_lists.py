from heapq import heapify, heappush, heappop


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        tmp_node = ListNode(0)
        start_node = tmp_node
        smallest_list = []

        for linked_list in lists:
            if linked_list is not None:
                smallest_list.append([linked_list.val, linked_list])

        heapify(smallest_list)

        while smallest_list:
            val_and_node = heappop(smallest_list)
            tmp_node.next = val_and_node[1]
            tmp_node = tmp_node.next

            if val_and_node[1].next:
                heappush(smallest_list, [val_and_node[1].next.val, val_and_node[1].next])

        return start_node.next


a = ListNode(1)
a.next = ListNode(3)
b = ListNode(2)
b.next = ListNode(4)
s = Solution()
c = s.mergeKLists([a, b])
while c:
    print c.val
    c = c.next
