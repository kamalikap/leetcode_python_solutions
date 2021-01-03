"""
94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [1,2]

"""
# Recursive: runtime-16ms

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.inorder(root, output)
        return output
        
    def inorder(self, root, output):
        if root is None:
            return
        
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)


# Iterative Runtime: 20 ms, faster than 70.13%

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        stack=[]
        
        while stack or root:
            
            if root:
                stack.append(root)
                root =root.left
                
            else:
                temp =stack.pop()
                output.append(temp.val)
                root= temp.right
           
        return output