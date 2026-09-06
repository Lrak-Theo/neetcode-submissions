# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        # Get the mid point using slow pointer and fast pointer
        s, f = head, head.next

        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        
        if f.next:
            s = s.next

        print(f"mid point value list: {s.val}")


        # Split the list into two halves
        # make the start of the second half be a head, where s.next is the new head
        l2 = s.next
        s.next = None
        l1 = head

        # Reverse the second half
        prev = None
        while l2:
            tmp_next = l2.next
            l2.next = prev
            prev = l2
            l2 = tmp_next
        l2 = prev
        # Then re-order the list using those two linked lists
        tail = ListNode()

        while l1 and l2: 
            next1 = l1.next
            next2 = l2.next

            tail.next = l1
            l1.next = l2
            tail = l2

            l1 = next1
            l2 = next2
        
        tail.next = l1 if l1 else l2


        


            








