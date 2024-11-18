class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, minimum, maximum):
            if not root:
                return True
            if not (minimum < root.val and root.val < maximum):
                return False
            return valid(root.left, minimum, root.val) and valid(root.right, root.val, maximum)

        return valid(root, float("-inf"), float("inf"))