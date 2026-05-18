# 2095. Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
# Attempts: 1

from typing import List, Optional, ValuesView


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def initializeList(self, arr: List[int]):
        curr = self
        for i in range(len(arr)):
            curr.val = arr[i]
            if i != len(arr) - 1:
                curr.next = ListNode()
                curr = curr.next

    def printList(self):
        print(self.val, end=" ")
        curr = self
        while curr.next:
            curr = curr.next
            print(curr.val, end=" ")
        print()


def deleteNode(head: Optional[ListNode]) -> Optional[ListNode]:
    # n = 1 case
    if head.next == None:
        return None

    fast = head
    slow = head

    while True:
        fast = fast.next
        if fast.next:
            fast = fast.next
            if not fast.next:
                break
        else:
            break
        slow = slow.next

    # Node deletion
    if slow.next:
        if slow.next.next:
            slow.next = slow.next.next
        else:
            slow.next = None

    return head


### TEST CASES
list1 = ListNode()
list1.initializeList([1, 3, 4, 7, 1, 2, 6])
list1.printList()
deleteNode(list1)
list1.printList()


list2 = ListNode()
list2.initializeList([1, 2, 3, 4])
list2.printList()
deleteNode(list2)
list2.printList()

list3 = ListNode()
list3.initializeList([2, 1])
list3.printList()
deleteNode(list3)
list3.printList()
