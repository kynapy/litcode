# 206. Reverse Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head == None:
            return
        if head.next == None:
            return head
        prev = head
        curr = head.next
        head.next = None
        while curr.next:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next
        curr.next = prev
        return curr