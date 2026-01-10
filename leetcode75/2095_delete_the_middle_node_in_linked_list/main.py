# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node count
        cnt = 0
        cur_node = head
        while cur_node:
            cnt += 1
            cur_node = cur_node.next
        # handle edge case
        if cnt == 1: 
            head = None
            return head
        
        pivot = 0
        middle_pos = math.floor(cnt / 2)
        middle_node = head
        prev_node = None
        while pivot < middle_pos:
            if pivot == middle_pos - 1:
                prev_node = middle_node
            middle_node = middle_node.next
            pivot += 1
        prev_node.next = middle_node.next
        middle_node.next = None
        return head
