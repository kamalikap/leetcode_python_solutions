"""
257. Binary Tree Paths : Runtime: 16 ms, faster than 93.92% of Python
https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        
        result = []
        self.dfs(root, "", result)
        return result

    def dfs(self, root, path, result):
        if not root.left and not root.right:
            result.append(path + str(root.val))
        
        if root.left:
            self.dfs(root.left, path + str(root.val) + "->" , result)
        if root.right:
            self.dfs(root.right, path + str(root.val) + "->", result)
