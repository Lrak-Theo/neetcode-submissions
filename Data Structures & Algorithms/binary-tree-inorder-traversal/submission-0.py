# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' recursive method'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def bstiot(r):
            if not r:
                return arr
            
            bstiot(r.left)

            arr.append(r.val)

            bstiot(r.right)

            return arr
        
        return bstiot(root)
