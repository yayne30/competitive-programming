# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.stack=[]

        def smallest(root):

            if not root:
                return 
            smallest(root.right)
            self.stack.append(root.val)
            smallest(root.left)
            


            # if not root:
            #     return 
            # self.stack.append(root.val)
            # smallest(root.left)
            # smallest(root.right)

        smallest(root)

        while self.stack and k>1:
            self.stack.pop()
            k -= 1
        return self.stack.pop()
        
        
        