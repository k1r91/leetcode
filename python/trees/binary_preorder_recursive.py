from typing import Optional, List
from tree import TreeNode


class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        output = list()
        output.append(root.val)
        self.traverse(root, output)
        return output

    def traverse(self, node: TreeNode, output: list):
        if node.left is not None:
            output.append(node.left.val)
            self.traverse(node.left, output)
        if node.right is not None:
            output.append(node.right.val)
            self.traverse(node.right, output)
