# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
            
        self.res=[]
        que=deque([root])
        flip=1

        while que:
            n=len(que)
            path=[]
            for _ in range(n):
                node=que.popleft()
                if node:
                    path.append(node.val)
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
            self.res.append(path[::flip])
            flip*=-1

        return self.res
            


            

                        
        