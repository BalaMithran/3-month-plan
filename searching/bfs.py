def bfs(root):
    if root != None:
        print(root.value)
        bfs(root.left)
        bfs(root.right)


def dfspostorder(root):
    if root.left != None and root.right != None:
        dfspostorder(root.left)
        dfspostorder(root.right)
        print(root.value)

    else:
        print(root.value)


def dfsinorder(root):
    if root.left != None and root.right != None:
        dfsinorder(root.left)
        print(root.value)
        dfsinorder(root.right)

    else:
        print(root.value)


def dfspreorder(root):
    if root.left != None and root.right != None:
        print(root.value)
        dfspreorder(root.left)
        dfspreorder(root.right)

    else:
        print(root.value)


class treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = treenode(5)
root.right = treenode(7)
root.left = treenode(2)
root.right.right = treenode(10)
root.right.left = treenode(6)


def printtree(root):
    if root != None:
        print(root.value)
        printtree(root.left)
        printtree(root.right)


dfsinorder(root)
