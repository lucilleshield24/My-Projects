class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
    def insert(self, new_node):
        if new_node.val > self.val:
            if self.right != None:
                self.right.insert(new_node)
            else:
                self.right = new_node
        else:
            if self.left != None:
                self.left.insert(new_node)
            else:
                self.left = new_node
    def lowest(self):
        if self.left != None:
            return self.left.lowest()
        else:
            return self.val
    # prints entire tree from lowest to highest
    def print_tree(self, node):
        result = self.lowest()
        return result


def make_tree():
    root = Node(7, None, None)
    for v in [10, 14, 6, 13, 8, 3, 4, 1]:
        n = Node(v, None, None)
        root.insert(n)
    return root

roots = make_tree()
print(roots.lowest())
print(roots.print_tree(roots))