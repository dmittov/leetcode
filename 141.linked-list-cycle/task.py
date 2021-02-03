# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        start = ListNode(None)
        start.next = head
        slow, fast = start, start
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            if fast == slow:
                return True
        return False
