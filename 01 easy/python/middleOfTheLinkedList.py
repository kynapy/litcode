# 876 https://leetcode.com/problems/middle-of-the-linked-list/description/
# Attempts: 1

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    if head:
        slow = head
        fast = head

        while True:
            if fast.next:
                fast = fast.next
            else: 
                break
            if slow.next:
                slow = slow.next
            if fast.next:
                fast = fast.next
            else:
                break


        return slow
