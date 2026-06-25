# 23. Merge K Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/
# Attempts: 1

from typing import List, Optional

import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for node in lists:
        # Empty list
        if not node:
            continue

        heapq.heappush(heap, node.val)
        while node.next:
            node = node.next
            heapq.heappush(heap, node.val)

    if not heap:
        return None

    curr = None
    result = None
    while heap:
        h = heapq.heappop(heap)
        if curr == None:
            curr = ListNode(h)
            result = curr
        else:
            new_node = ListNode(h)
            curr.next = new_node
            curr = new_node

    return result
