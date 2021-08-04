# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None
        
        pre = head
        cur = head

        for i in range(n):
            cur = cur.next
        if cur == None:
            return head.next
        
        pre_pre = pre
        pre = pre.next
        cur = cur.next

        while cur != None:
            pre_pre = pre_pre.next
            pre = pre.next
            cur = cur.next
        
        pre_pre.next = pre.next

        
        return head