# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.f=True
        def tree(p,q):
            if p and q and p.val==q.val:
                tree(p.left,q.left)
                tree(p.right,q.right)
            elif not p and not q:
                return
            else:
                self.f=False
        tree(p,q)
        return self.f
        

        
        