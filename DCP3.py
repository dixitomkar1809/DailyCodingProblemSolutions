# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.serializeDFS(root, "")
    
    def serializeDFS(self, root, string):
        if root is None:
            string+=("None"+" ")
        else:
            string+=(str(root.val)+" ")
            string = self.serializeDFS(root.left, string)
            string = self.serializeDFS(root.right, string)
        return string
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None
        data = data.strip().split(" ")
        return self.deserializeHelper(data)
    
    def deserializeHelper(self, data):
        if data[0]=="None":
            data.pop(0)
            return None
        root = TreeNode(int(data.pop(0)))
        root.left = self.deserializeHelper(data)
        root.right = self.deserializeHelper(data)
        return root
         

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))