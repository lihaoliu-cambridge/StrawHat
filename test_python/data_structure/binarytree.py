class BinaryTree(object):
    def __init__(self, root_value):
        self.value = root_value
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node_value):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node_value)
        else:
            tmp_node = BinaryTree(new_node_value)
            tmp_node.left_child, self.left_child = self.left_child, tmp_node

    def insert_right(self, new_node_value):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node_value)
        else:
            tmp_node = BinaryTree(new_node_value)
            tmp_node.right_child, self.right_child = self.right_child, tmp_node

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

r = BinaryTree('a')
print(r.get_value())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_value())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_value())
r.get_right_child().set_value('hello')
print(r.get_right_child().get_value())
