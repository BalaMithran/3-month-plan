
class Solution:

    def levelOrder(self, root):
        queue = []
        queue.append(root)
        listt = []
        while True:
            if len(queue) == 0:
                break
            node = queue.pop(0)
            listt.append(node.data)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return listt
