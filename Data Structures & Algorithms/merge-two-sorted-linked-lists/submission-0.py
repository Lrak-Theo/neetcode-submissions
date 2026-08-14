# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        tail = dummy_node

        current_l = list1
        current_r = list2

        while current_l and current_r:
            if current_l.val > current_r.val:
                tail.next = current_r
                current_r = current_r.next
            
            else:
                tail.next = current_l
                current_l = current_l.next
            
            tail = tail.next
        
        if current_l:
            tail.next = current_l
        else:
            tail.next = current_r

        return dummy_node.next
            

'''
Merge sort in the form of linked list 

do we need to make a new list? --> try that first

two pointer approach:

list 1 and list 2 are both heads
1 2 4 <- tail? << yes
1 3 5 <- tail? << yes

'''