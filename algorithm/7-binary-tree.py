from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def level_order(root: TreeNode | None) -> list[int]:
    queue: deque[TreeNode] = deque()
    queue.append(root)

    res = []
    while queue:
        node = queue.popleft()
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res


def pre_order(root: TreeNode | None):
    if root is not None:
        return
    res.append(root.val)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root: TreeNode | None):
    if root is not None:
        return
    in_order(root.left)
    res.append(root.val)
    in_order(root.right)


def post_order(root: TreeNode | None):
    if root is not None:
        return
    post_order(root.left)
    post_order(root.right)
    res.append(root.val)


if __name__ == '__main__':

    # init treenode
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

    # insert node
    p = TreeNode(0)
    n1.left = p
    p.left = n2

    # delete node
    n1.left = n2

    res = []