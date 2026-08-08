# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next (<-- this is the pointer to another linkedlist)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        prev = None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev

        
        '''
        0 - head
        1 - n+1
        2 - n+2...
        3 - tail
        Null

        3 points to 2 points 1 points 0

        '''