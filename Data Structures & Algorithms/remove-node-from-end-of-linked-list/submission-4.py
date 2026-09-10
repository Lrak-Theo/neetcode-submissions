# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        length = 0
        counter = 0

        if n == 1 and node.next == None:
            node = None
            return node

        # approach 1: get the lenght of the pointer then length - n = position in asc
        while node:
            node = node.next
            length += 1

        index = length - n
        print(index)
        node = head

        while node:

            if counter == index:
                if counter == 0:
                    head = node.next
                    return head
                last_node.next = node.next
                return head

            last_node = node
            node = node.next
            counter += 1
        
    
