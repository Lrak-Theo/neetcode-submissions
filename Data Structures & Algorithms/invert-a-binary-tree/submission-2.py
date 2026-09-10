# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(r):
            if not r:
                return r


            dfs(r.left)
            dfs(r.right)

            left_reference = r.left
            r.left = r.right
            r.right = left_reference

        
        dfs(root)
        return root
        
 
