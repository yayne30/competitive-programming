# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.ans=None
        def search(root,val):
            if not root:
                return
            if root.val==val:
                self.ans=root
            search(root.left,val)
            search(root.right,val)
        search(root,val)
        return self.ans
        
        


















        # if not root:
        #     return None
        # if root.val==val:
        #     return root
        # if root.val>val:
        #     return self.searchBST(root.left,val)
        # else:
        #     return self.searchBST(root.right,val)
        

        # # while root:
        # #     if root.val==val:
        # #         return root
        # #     elif root.val>val:
        # #         root=root.left
        # #     elif root.val<val:
        # #         root=root.right
        # # return None
    