# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total=0
        def sumnum(root,valu):
            if not root:
                return 
            if not root.left and not root.right:
                self.total+=(root.val+valu)
                return root.val+valu
            if root.left or root.right:
                valu=(valu+root.val) * 10
            sumnum(root.left,valu)
            sumnum(root.right,valu)

        sumnum(root,0)
        return self.total
            
            

        

        