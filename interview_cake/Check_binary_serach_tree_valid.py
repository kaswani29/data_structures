class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def bst_validator(root):
    nodes_bound_stack = [(root, -float('inf'), -float('inf'))]

    while len(nodes_bound_stack):

        current_node, lower_bound, upper_bound = nodes_bound_stack.pop()

        if current_node <= lower_bound or current_node >= upper_bound:
            return False

        if current_node.left:
            nodes_bound_stack.append((current_node.left, lower_bound, current_node.value))

        if current_node.right:
            nodes_bound_stack.append((current_node.right, current_node.value, upper_bound))

    return True