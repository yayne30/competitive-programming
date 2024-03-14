# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        value = max(nums)
        node = TreeNode(value)
        ind = nums.index(value)
        if len(nums) == 1:
            return node
        if ind != 0:
            node.left = self.constructMaximumBinaryTree(nums[0 : ind])
        elif ind == 0:
            node.left == None
        if ind < len(nums) - 1:
            node.right = self.constructMaximumBinaryTree(nums[ind + 1:])
        elif ind == len(nums) - 1:
            node.right = None
        return node


        