import math
# Online Python - IDE, Editor, Compiler, Interpreter
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class ListNode:
    def __init__(self):
        self.head = None
    
    def insertNode(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    def deleteFirstNode(self):
        new_head = self.head.next
        self.head = new_head
    
    def findMiddleNode(self):
        cnt = 0
        cur_node = self.head
        while cur_node:
            cnt += 1
            cur_node = cur_node.next
        pivot = 0
        middle_pos = math.floor(cnt / 2)
        middle_node = self.head
        prev_node = None
        while pivot < middle_pos:
            if pivot == middle_pos - 1:
                prev_node = middle_node
            middle_node = middle_node.next
            pivot += 1
        prev_node.next = middle_node.next
        middle_node.next = None
    
    def oddEventList(self):
        if self.head is None or self.head.next is None:
            return None
        odd, even = self.head, self.head.next
        first_even_node = self.head.next
        
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = first_even_node
    
    def printList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.val)
            cur_node = cur_node.next

ln = ListNode()
ln.insertNode(6)
ln.insertNode(5)
ln.insertNode(4)
ln.insertNode(3)
ln.insertNode(2)
ln.insertNode(1)

ln.oddEventList()
# ln.findMiddleNode()
ln.printList()

