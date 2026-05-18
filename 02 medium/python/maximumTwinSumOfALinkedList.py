# 2130. Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
# Attempts: 1

from typing import List, Optional


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


# Stack solution
# - non destructive
# - O(n) space
def pairSum(head: Optional[ListNode]) -> int:
    num_nodes = 1
    count_pointer = head

    while count_pointer.next:
        count_pointer = count_pointer.next
        num_nodes += 1

    stack = []
    curr = head
    for i in range(num_nodes // 2):
        stack.append(curr.val)
        curr = curr.next

    max_sum = 0
    for i in range(num_nodes // 2):
        curr_sum = curr.val + stack.pop(-1)
        if curr_sum > max_sum:
            max_sum = curr_sum
        curr = curr.next

    return max_sum


# Two-pointer pointer flip solution
# - inplace, O(1) space
# - destructive
def pairSumPointerFlip(head: Optional[ListNode]) -> int:
    # Find second half
    front_pointer = head.next
    back_pointer = head
    while front_pointer.next:
        back_pointer = back_pointer.next
        front_pointer = front_pointer.next.next

    # Flip second half nodes
    curr_pointer = back_pointer.next
    back_pointer.next = None

    next_pointer = curr_pointer.next
    while next_pointer:
        temp = None
        if next_pointer.next:
            temp = next_pointer.next

        next_pointer.next = curr_pointer
        curr_pointer = next_pointer
        next_pointer = temp

    # Find max sum
    curr = head
    max_sum = head.val + front_pointer.val
    while head.next:
        head = head.next
        front_pointer = front_pointer.next

        curr_sum = head.val + front_pointer.val
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum


### TEST CASES
ln1 = ListNode()
ln1.initializeList([5, 4, 2, 1])
print(pairSumPointerFlip(ln1))

ln2 = ListNode()
ln2.initializeList([4, 2, 2, 3])
print(pairSumPointerFlip(ln2))

ln3 = ListNode()
ln3.initializeList([1, 100000])
print(pairSumPointerFlip(ln3))
