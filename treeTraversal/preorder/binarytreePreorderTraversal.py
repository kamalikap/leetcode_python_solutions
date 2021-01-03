"""
144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]

Example 5:
Input: root = [1,null,2]
Output: [1,2]

"""

# Recursive solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output =[]
        self.dfs(root, output)
        return output
    
    def dfs(self, root, output):
        if root is None:
            return
        
        output.append(root.val)
        self.dfs(root.left, output)
        self.dfs(root.right, output)
       
	   
# Iterative Solution- Runtime: 12 ms, faster than 97.82%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output =[]
        stack = [root]
        
        while stack:
            temp=stack.pop()
            if temp:
                output.append(temp.val)
                stack.append(temp.right)
                stack.append(temp.left)
        
        return output
