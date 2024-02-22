# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def traverse(root):
            if root==None:
                return res
            res.append(root.val)
            traverse(root.left)
            traverse(root.right)
            return res
        return traverse(root)
        
        



        # def travers(root):
        #     if root:
        #         if root.left==None and root.right==None:
        #             return root.val
        #         travers(root.left)
        #         travers(root.right)
        # res.append(travers(root))
        # return res
        
        
        
    
        


        