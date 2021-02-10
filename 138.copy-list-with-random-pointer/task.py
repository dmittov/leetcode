# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def enumerate_copyRandomList(self, head: "Node") -> "Node":
        idx = 0
        origin_addr2idx = dict()
        copy_idx2addr = dict()
        copy_head = Node(0)
        copy_current = copy_head
        origin_head = head
        while origin_head:
            origin_addr2idx[origin_head] = idx
            new_node = Node(origin_head.val)
            copy_idx2addr[idx] = new_node
            copy_current.next = new_node
            copy_current = copy_current.next
            idx += 1
            origin_head = origin_head.next
        origin_head = head
        copy_current = copy_head
        while origin_head:
            if origin_head.random:
                idx = origin_addr2idx[origin_head.random]
                copy_addr = copy_idx2addr[idx]
                copy_current.next.random = copy_addr
            copy_current = copy_current.next
            origin_head = origin_head.next
        return copy_head.next

    @staticmethod
    def __duplicate(head: "Node") -> None:
        while head:
            node_copy = Node(head.val, next=head.next, random=head.random)
            head.next = node_copy
            head = node_copy.next

    @staticmethod
    def __split(head: "Node") -> None:
        while head:
            new_node = head.next
            head = head.next.next
            if new_node.random:
                new_node.random = new_node.random.next
            if head:
                new_node.next = head.next

    def duplicate_copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return None
        self.__duplicate(head)
        origin_list, copy_list = head, head.next
        self.__split(head)
        return copy_list

    def copyRandomList(self, head: "Node") -> "Node":
        return self.duplicate_copyRandomList(head)
