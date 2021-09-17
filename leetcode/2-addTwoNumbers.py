# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        addDigit = 0
        # ans = ListNode()

        if l1 == None or l2 == None:
            return l1 if l1 == None else l2
        
        # head = ans
        ans = l1

        while l1.next != None and l2.next != None:
            l1.val = l1.val + l2.val + addDigit
            addDigit = l1.val // 10
            l1.val = l1.val % 10
            l1 = l1.next
            l2 = l2.next
        
        l1.val = l1.val + l2.val + addDigit
        addDigit = l1.val // 10
        l1.val = l1.val % 10

        if l1.next == None:
            if l2.next == None:
                if addDigit == 0:
                    return ans
                else:
                    l1.next = ListNode(addDigit, None)
                    return ans
            else:
                l1.next = l2.next
                l2 = l2.next
                while l2.next != None:
                    l2.val = l2.val + addDigit
                    addDigit = l2.val // 10
                    l2.val = l2.val % 10
                    l2 = l2.next
                
                l2.val = l2.val + addDigit
                addDigit = l2.val // 10
                l2.val = l2.val % 10

                if addDigit == 0:
                    return ans
                else:
                    l2.next = ListNode(addDigit, None)
                    return ans
        else:
            l1 = l1.next
            while l1.next != None:
                l1.val = l1.val + addDigit
                addDigit = l1.val // 10
                l1.val = l1.val % 10
                l1 = l1.next
                
            l1.val = l1.val + addDigit
            addDigit = l1.val // 10
            l1.val = l1.val % 10

            if addDigit == 0:
                return ans
            else:
                l1.next = ListNode(addDigit, None)
                return ans

