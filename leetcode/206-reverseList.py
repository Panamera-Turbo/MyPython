# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
            
        tail = head
        while tail.next != None:
            tail = tail.next

        newHead = tail
        while head != tail:
            p = head
            head = head.next
            p.next = newHead.next
            newHead.next = p
            


        return newHead