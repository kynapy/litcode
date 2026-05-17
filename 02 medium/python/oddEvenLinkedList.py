# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/description/
# Attempts: 3

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printChain(self):
        curr = self
        print(self.val, end=", ")
        while curr.next:
            curr = curr.next
            print(curr.val, end=", ")
        print()

    def populateChain(self, ls: List[int]):
        curr = self
        for i in range(len(ls)):
            curr.val = ls[i]
            if i != len(ls) - 1:
                curr.next = ListNode()
                curr = curr.next


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    count = 1
    even_head = ListNode()
    even_tracker = even_head
    curr = head

    while curr.next:
        count += 1
        if count % 2 == 0:
            temp = curr.next
            curr.next = temp.next
            even_tracker.next = temp
            even_tracker = even_tracker.next
            if curr.next:
                curr = curr.next

    even_tracker.next = None
    if even_head.next:
        curr.next = even_head.next

    return head


### TEST CASES

# TEST CASE 1
test1 = ListNode()
test1.populateChain([1, 2, 3, 4, 5])
oddEvenList(test1)
test1.printChain()

# TEST CASE 2
test2 = ListNode()
test2.populateChain([2, 1, 3, 5, 6, 4, 7])
oddEvenList(test2)
test2.printChain()


# TEST CASE 3
test3 = ListNode()
test3.populateChain([1, 2, 3, 4, 5, 6, 7, 8])
oddEvenList(test3)
test3.printChain()
