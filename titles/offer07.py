# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from dataStructer.binary_tree import TreeNode, pre_order_traversal, in_order_traversal


class Solution(object):
    def buildTree(self, preorder:list, inorder:list)->TreeNode:
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        index = inorder.index(preorder[0])

        left_pre = preorder[1:index+1]
        left_in = inorder[:index]
        right_pre = preorder[index+1:]
        right_in = inorder[index+1:]

        node.left = self.buildTree(left_pre,left_in)
        node.right = self.buildTree(right_pre,right_in)

        return node

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
so = Solution()
node = so.buildTree(preorder,inorder)
pre_order_traversal(node)
in_order_traversal(node)

