# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def bst(root,miv=float('-inf'),mxv=float('inf')):
            if root==None:
                return True
            
            if not (miv<root.val<mxv):
                return False
            
            return (bst(root.left,miv,root.val) and
                   bst(root.right,root.val,mxv))
        return bst(root)



        # if root and not root.left and not root.right:
        #     return True

        # elif not root.left and root.val<root.right.val:
        #     return True

        # elif not root.right and root.val>root.left.val:
        #     return True
        # elif root.left and root.right:

        #     if root.val>root.left.val and root.val<root.right.val:
        #         return True
        # else:
        #     return False
        # return self.isValidBST(root.left) and self.isValidBST(root.right)


        
        
        

        # self.check=True

        # def valid(root):
            

        
        # return self.check




        # self.check=True

        # def valid(root):

        #     if not root.left and not root.right:
        #         return root

        #     if root.val < valid(root.right).val:
        #         self.check=False

        #     elif root.val > valid(root.left).val:
        #         self.check=False
        # valid(root)
        # return self.check

            
        
        