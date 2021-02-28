from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int):
        indorder = []
        Solution.inorder(root, indorder)
        total_sum = 0

        for val in indorder:
            if val >= low and val <= high:
                total_sum += val

        return total_sum

    def makeTree(self, input):
        input = [None] + input
        length = len(input)

        def makeNode(index):
            if index >= length or input[index] == None:
                return None
            return TreeNode(input[index], makeNode(index * 2), makeNode(index * 2 + 1))

        return makeNode(1)

    @staticmethod
    def preorder(node: TreeNode, path: List):
        if node == None:
            return
        path.append(node.val)
        Solution.preorder(node.left, path)
        Solution.preorder(node.right, path)

    @staticmethod
    def inorder(node: TreeNode, path: List):
        if node == None:
            return
        Solution.inorder(node.left, path)
        path.append(node.val)
        Solution.inorder(node.right, path)


s = Solution()
i = [10, 5, 15, 3, 7, None, 18]
root = s.makeTree(i)

o = s.rangeSumBST(root, 7, 15)
print(o)
