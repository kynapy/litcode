# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1,  l2):
        first = l1.val + l2.val
        if first > 9:
            remainder = 1
            first = first % 10
        else:
            remainder = 0
        result = ListNode(first)
        currPointer = result
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            currVal = l1.val + l2.val + remainder
            if currVal > 9:
                currVal = currVal % 10
                remainder = 1
            else:
                remainder = 0
            currPointer.next = ListNode(currVal)
            currPointer = currPointer.next

        # accounting for leftovers
        if l1.next:
            while l1.next:
                l1 = l1.next
                currVal = l1.val + remainder
                if currVal > 9:
                    currVal = currVal % 10
                    remainder = 1
                else:
                    remainder = 0
                currPointer.next = ListNode(currVal)
                currPointer = currPointer.next
        elif l2.next:
            while l2.next:
                l2 = l2.next
                currVal = l2.val + remainder
                if currVal > 9:
                    currVal = currVal % 10
                    remainder = 1
                else:
                    remainder = 0
                currPointer.next = ListNode(currVal)
                currPointer = currPointer.next

        if remainder:
            currPointer.next = ListNode(1)

        return result