# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        stack = []

        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            popped_node = stack.pop()
            arr.append(popped_node.val)
            node = popped_node.right
 
        return arr