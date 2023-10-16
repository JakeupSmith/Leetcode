# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def inorder(root):
            if not root: #if it exists.
                return 
            inorder(root.left) #left side tree of node
            res.append(root.val) #take in the values of the node
            inorder(root.right) #right side tree of the node (moves throughout the tree from left to right hence "inorder")
        
        inorder(root)
        return res