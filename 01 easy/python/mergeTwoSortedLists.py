# Defining my own ListNode class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        print("[", end="")
        if self.val:
            print(self.val, end=", ")
        curr = self.next
        while curr:
            print(curr.val, end=", ")
            curr = curr.next
        print("]")

# Defining my own LinkedList class
class LinkedList(object):
    def __init__(self, list):
        # Empty list
        self.size = 0
        self.head = None

        # Non-empty List
        if list:
            self.head = ListNode(list[0])
            self.size = 1
            curr = self.head
            for i in range(1, len(list)):
                curr.next = ListNode(list[i])
                curr = curr.next
                self.size += 1

    def printList(self):
        print("[", end="")
        curr = self.head
        for i in range(self.size):
            print(curr.val, end=", ")
            curr = curr.next
        print("]")

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Both lists are empty
        if not list1 and not list2:
            return list1

        # One of the lists are empty
        if not list1:
            return list2
        if not list2:
            return list1

        # Both lists aren't empty
        resultHead = ListNode()
        curr = resultHead
        while list1 and list2: # Runs until one list is empty
            if list1.val < list2.val:
                curr.val = list1.val
                list1 = list1.next
            else: # Covers the case if they are equal
                curr.val = list2.val
                list2 = list2.next
            curr.next = ListNode()
            curr = curr.next


        # Pushing one empty list and one non-empty list to the result list
        if list1:
            curr.val = list1.val
            curr.next = list1.next
        else:
            curr.val = list2.val
            curr.next = list2.next
        return resultHead

# Test Cases
test = Solution()
test.mergeTwoLists(LinkedList([-9,3]).head, LinkedList([5,7]).head).printList()
# print(test.mergeTwoLists([], []))