# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = []
        q = deque()
        root.val = 0
        q.append(root)
        max_width = 0
        while q:
            curr_width = len(q)
            max_width = max(max_width , (q[-1].val - q[0].val) + 1)
            while curr_width > 0:
                temp = q.popleft()
                curr_width -= 1
                if temp.left:
                    temp.left.val = (temp.val * 2 )+ 1
                    q.append(temp.left)
                if temp.right:
                    temp.right.val = (temp.val * 2) + 2
                    q.append(temp.right)

        return max_width






            
        