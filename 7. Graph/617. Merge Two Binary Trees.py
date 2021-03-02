# Definition for a binary tree node.
import operator


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode):
        def bfs(root: TreeNode):
            if not root:
                return []
            queue = [root]
            tree = []
            while len(queue) > 0:
                node = queue.pop(0)
                tree.append(node.val)

                if node.left:
                    queue.append(node.left)
                else:
                    if node.right:
                        queue.append(TreeNode(None))

                if node.right:
                    queue.append(node.right)
                else:
                    if node.left:
                        queue.append(TreeNode(None))
            return tree

        tree1 = bfs(root1)
        tree2 = bfs(root2)
        size1 = len(tree1)
        size2 = len(tree2)
        maxsize = max(size1, size2)

        tree3 = [None] * maxsize
        for i in range(maxsize):
            node1 = tree1[i] if (i < size1) else None
            node2 = tree2[i] if (i < size2) else None
            if node1 == None and node2 == None:
                continue
            tree3[i] = (0 if not node1 else node1) + (0 if not node2 else node2)
        print(tree3)
        # return self.makeTree(tree3)

    def makeTree(self, input):
        input = [None] + input
        length = len(input)

        def makeNode(index):
            if index >= length or input[index] == None:
                return None
            return TreeNode(input[index], makeNode(index * 2), makeNode(index * 2 + 1))

        return makeNode(1)


s = Solution()
i1, i2 = [1, 2, None, 3], [1, None, 2, None, 3]
r1, r2 = s.makeTree(i1), s.makeTree(i2)
o = s.mergeTrees(r1, r2)
