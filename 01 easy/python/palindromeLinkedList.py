# 234. Palindrome Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        ls = [head.val]
        while head.next:
            head = head.next
            ls.append(head.val)
        for i in range(len(ls) // 2):
            if ls[i] != ls[-i-1]:
                return False
        return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(Solution().isPalindrome(head))

head = ListNode(1)
head.next = ListNode(2)
print(Solution().isPalindrome(head))