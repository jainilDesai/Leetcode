# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def isSorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] >= arr[i+1]:
                    return False
            return True
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        return isSorted(arr)