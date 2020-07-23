class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def _isValidBSTHelper(self, node: Node, low, high):
        """
        Recursive version of checking if the Binary Tree is valid or not
        """
        if not node:
            return True
        val = node.val
        if (val > low and val < high) and self._isValidBSTHelper(node.left, low, node.val) and self._isValidBSTHelper(node.right, node.val, high):
            return True
        return False

    def isValidBST(self, node: Node) -> bool:
        return self._isValidBSTHelper(node, float('-inf'), float('inf'))


if __name__ == '__main__':
    node = Node(5)
    node.left = Node(4)
    node.right = Node(7)
    node.right = Node(2)
    print(Solution().isValidBST(node))
