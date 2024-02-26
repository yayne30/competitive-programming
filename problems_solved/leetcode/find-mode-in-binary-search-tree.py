# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dictt={}
        count=[]
        def recur(root):
            if root==None:
                return
            self.dictt[root.val]=self.dictt.get(root.val,0)+1
            recur(root.left)
            recur(root.right)
        recur(root)
        for i in self.dictt:
            m=max(self.dictt.values())
            if self.dictt[i]==m:
                count.append(i)


        return count

        
            

        