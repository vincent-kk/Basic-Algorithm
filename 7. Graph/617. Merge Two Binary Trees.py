# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode):
        def merging(augend: TreeNode, addend: TreeNode):
            if not augend:
                return addend
            if not addend:
                return augend
            augend.val = augend.val + addend.val
            augend.left = merging(augend.left, addend.left)
            augend.right = merging(augend.right, addend.right)
            return augend

        return merging(root1, root2)

    def makeTree(self, input):
        input = [None] + input
        length = len(input)

        def makeNode(index):
            if index >= length or input[index] == None:
                return None
            return TreeNode(input[index], makeNode(index * 2), makeNode(index * 2 + 1))

        return makeNode(1)

    @staticmethod
    def bfs(root: TreeNode):
        queue = [root]
        path = []
        while len(queue) > 0:
            node = queue.pop(0)
            path.append(node.val)
            if node.left:
                queue.append(node.left)
            if not node.left and node.right:
                queue.append(TreeNode(None))
            if node.right:
                queue.append(node.right)

        return path


s = Solution()
i1, i2 = [1, 3, 2, 5], [2, 1, 3, None, 4, None, 7]
r1, r2 = s.makeTree(i1), s.makeTree(i2)
o = s.mergeTrees(r1, r2)
array = Solution.bfs(o)
for e in array[:-1]:
    print(e, end=">")
print(array[-1])