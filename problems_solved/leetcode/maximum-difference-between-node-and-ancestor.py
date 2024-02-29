# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_diff=0 
        

        def maxance(root,minvalue,maxvalue):
             
            if not root:
                return
            if root.val<minvalue:
                minvalue=root.val

            elif root.val>maxvalue:
                maxvalue=root.val
            
            self.max_diff=max(self.max_diff,abs(maxvalue-minvalue))
            maxance(root.left,minvalue,maxvalue)
            maxance(root.right,minvalue,maxvalue)
            return self.max_diff

        return maxance(root,root.val,root.val)
        
        
            

    
            
        
        