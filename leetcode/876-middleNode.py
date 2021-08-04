# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        pre = head
        cur = head
        while cur != None and cur.next != None:
            pre = pre.next
            cur = cur.next.next
        
        return pre