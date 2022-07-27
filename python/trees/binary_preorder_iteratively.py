from typing import Optional, List
from tree import TreeNode


class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        tree_list, output = [root], list()
        while tree_list:
            node = tree_list.pop()
            output.append(node.val)
            if node.right is not None:
                tree_list.append(node.right)
            if node.left is not None:
                tree_list.append(node.left)
        return output