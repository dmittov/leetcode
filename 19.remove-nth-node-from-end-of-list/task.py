class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre_remove = head
        scout = head
        for _ in range(n):
            if not scout:
                return head
            scout = scout.next

        # corner case
        if not scout:
            return head.next
        scout = scout.next

        while scout:
            scout = scout.next
            pre_remove = pre_remove.next

        pre_remove.next = pre_remove.next.next
        return head
