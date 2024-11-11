# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input = root of a binary tree
# output = list of values in each level of the tree
# using level order traversal (left to right, level by level)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]

        while queue:
            current_level = []
            for _ in range(len(queue)):
                # get current node
                node = queue.pop(0)
                # add value to current level
                current_level.append(node.val)
                # add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # add current level to result
            result.append(current_level)
        return result



