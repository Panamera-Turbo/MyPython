# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None or root.right == None:
            return root
        
        root.left.next = root.right
        
        self.connect(root.left).next
        self.connect(root.right) 

        if root.next == None:
            return root
        
        root.right.next = root.next.left

        self.connect(root.right).next
        self.connect(root.next.left)

        return root