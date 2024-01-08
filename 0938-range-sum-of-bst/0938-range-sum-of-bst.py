# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def search(root):
            if not root: return 0
            res=0
        
            if high>=root.val>=low:
                res+=root.val
            if root.val<high:
                res+=search(root.right)
            if root.val>low:
                res+=search(root.left)

            return res
        return search(root)