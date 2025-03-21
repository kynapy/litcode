# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    slow_pointer, fast_pointer = head, head
    countdown = n
    if fast_pointer.next == None:
        return None
    else:
        while fast_pointer.next:
            fast_pointer = fast_pointer.next
            if countdown == 0:
                slow_pointer = slow_pointer.next
            else:
                countdown -= 1
        if countdown == 0:
            slow_pointer.next = slow_pointer.next.next
        else:
            head = head.next
        return head

# Testing functions
def testRemoveNthFromEnd(array, n):
    head = ListNode(array[0])
    curr = head
    for i in range(1, len(array)):
        new_node = ListNode(array[i])
        curr.next = new_node
        curr = curr.next

    printListNode(removeNthFromEnd(head ,n))

def printListNode(head):
    if head == None:
        print([])
        return
    while head.next:
        print(head.val, end=", ")
        head = head.next
    print(head.val)

# Test cases
testRemoveNthFromEnd([1,2,3,4,5], 2)
testRemoveNthFromEnd([1], 1)
testRemoveNthFromEnd([1,2], 1)
testRemoveNthFromEnd([1,2], 2)
