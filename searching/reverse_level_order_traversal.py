class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
def reverseLevelOrder(root):
        queue = []
        queue.append(root)
        listt = []
        while True:
            if len(queue) == 0:
                break
            node = queue.pop(0)
            listt.append(node.data)
            if node.right != None:
                queue.append(node.right)
            if node.left != None:
                queue.append(node.left)
            
        return listt[::-1]
