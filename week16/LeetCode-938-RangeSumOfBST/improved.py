# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sumBST = 0
        def dfs(node):
            if not node:
                return 0
            
            nonlocal sumBST
            if(node.val < low):
                return dfs(node.right)
                
            elif(node.val > high):
                return dfs(node.left)

            sumBST += node.val
            dfs(node.right)
            dfs(node.left)
            return 0
        
        dfs(root)
        return sumBST