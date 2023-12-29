# 141. Linked List Cycle

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if head == None:
            return False
        curr = head
        while curr.next:
            if curr.next == head:
                return True
            else:
                next = curr.next
                curr.next = head
                curr = next
        return False