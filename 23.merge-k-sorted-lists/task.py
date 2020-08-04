import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeAdapter:
    
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    
    def init(self, lists: List[ListNode]) -> List[Optional[ListNode]]:
        pointers = [ListNodeAdapter(lst) for lst in lists if lst]
        heapq.heapify(pointers)
        return pointers
        
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = self.init(lists)        
        if not heap:
            return None
        current_item = heapq.heappop(heap)
        head = ListNode(current_item.node.val)
        current_list_item = head
        if current_item.node.next:
            heapq.heappush(heap, ListNodeAdapter(current_item.node.next))
        while heap:
            current_item = heapq.heappop(heap)
            next_list_item = ListNode(current_item.node.val)
            current_list_item.next = next_list_item
            current_list_item = next_list_item
            if current_item.node.next:
                heapq.heappush(heap, ListNodeAdapter(current_item.node.next))
        return head
