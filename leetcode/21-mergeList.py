# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        
        if l2 == None:
            return l1

        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        q = head
        while l1 != None and l2 != None:
            if l1.val > l2.val:
               p = l2
               l2 = l2.next
               q.next = p
               q = q.next
            else:
               p = l1
               l1 = l1.next
               q.next = p
               q = q.next

        if l1 != None:
            q.next = l1
        elif l2 != None:
            q.next = l2

        return head