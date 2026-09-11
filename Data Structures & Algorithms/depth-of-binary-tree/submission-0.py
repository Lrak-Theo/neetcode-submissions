# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        h = 0
        arr = []

        def dfs(r, h, arr):
            if not r:
                return arr

            h += 1
            arr.append(h)
            dfs(r.left, h, arr)
            dfs(r.right, h, arr)

        dfs(root, h, arr)

        return max(arr) if arr else 0
