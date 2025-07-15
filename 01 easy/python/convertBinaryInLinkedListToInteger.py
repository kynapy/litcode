# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head: ListNode):
    binary_number = ''
    result = 0
    while head.next:
        binary_number += str(head.val)
        head = head.next
    binary_number += str(head.val)
    
    for i in range(1, len(binary_number) + 1):
        result += 2 ** (i - 1) * int(binary_number[-i])

    return result

def createLinkedList(num_list: list):
    head = ListNode(num_list[0])
    current = head
    for i in range(1, len(num_list)):
        current.next = ListNode(num_list[i])
        current = current.next

    return head


### TEST CASES ###
print(getDecimalValue(createLinkedList([1,0,1])))
print(getDecimalValue(createLinkedList([0])))
print(getDecimalValue(createLinkedList([1,1,1,1])))
