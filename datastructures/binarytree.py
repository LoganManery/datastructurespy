class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    if self.root is None:
      self.root = TreeNode(value)
    else:
      self._insert_recursive(self.root, value)

  def _insert_recursive(self, current_node, value):
    if value < current_node.value:
      if current_node.left is None:
        current_node.left = TreeNode(value)
      else:
        self._insert_recursive(current_node.left, value)
    else:
      if current_node.right is None:
        current_node.right = TreeNode(value)
      else:
        self._insert_recursive(current_node.right, value)

  def contains(self, value):
    return self._contains_recursive(self.root, value)
  
  def _contains_recursive(self, current_node, value):
    if current_node is None:
      return False
    if current_node.value == value:
      return True
    elif value < current_node.value:
      return self._contains_recursive(current_node.left, value)
    else:
      return self._contains_recursive(current_node.right, value)
    
  def print_tree(self):
    self._print_tree_recursive(self.root, 0)

  def _print_tree_recursive(self, node, level):
    if node is not None:
      self._print_tree_recursive(node.right, level + 1)
      print(' ' * 4 * level + '->', node.value)
      self._print_tree_recursive(node.left, level + 1)