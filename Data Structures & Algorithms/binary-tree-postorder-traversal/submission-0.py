# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr, stack = [], []
        node = root
        last_visited = None
        
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
                
            parent = stack[-1]

            if parent.right and parent.right != last_visited:
                node = parent.right
            else:
                popped_node = stack.pop()
                arr.append(popped_node.val)
                last_visited = popped_node
                node = None
            # Put logic at the end

        return arr
        ''' brute force 
        def dfs_po(r):
            if not r:
                return
            
            dfs_po(r.left)
            dfs_po(r.right)

            arr.append(r.val)
        dfs_po(root)
        '''

        