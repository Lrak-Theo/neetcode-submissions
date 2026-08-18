# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        fast_node = head
        

        while fast_node and fast_node.next:
            node = node.next
            fast_node = fast_node.next.next

            if fast_node == node:
                return True

        return False

            