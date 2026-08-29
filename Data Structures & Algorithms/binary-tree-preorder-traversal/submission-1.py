# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        array = []

        def preorder(r):

            if not r:
                return array
            
            array.append(r.val) # Append the value as we travel through each nodes

            preorder(r.left) # Check left subtree first until leaf is hit

            preorder(r.right) # Then check right subtree

        preorder(root)

        return array # Time complexity of: O(V + E)