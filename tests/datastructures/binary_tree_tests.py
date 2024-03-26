import unittest
from datastructures.binarytree import BinaryTree

class TestBinaryTree(unittest.TestCase):
  def test_insert_and_search(self):
    tree = BinaryTree()
    values_to_insert = [5, 3, 7, 2, 4, 6, 8]

    for value in values_to_insert:
      tree.insert(value)

    for value in values_to_insert:
      self.assertTrue(tree.contains(value))
    self.assertFalse(tree.contains(10))

  def test_empty_tree_search(self):
    tree = BinaryTree()
    self.assertFalse(tree.contains(1))

  def test_structure(self):
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)

    self.assertEqual(tree.root.value, 5)
    self.assertEqual(tree.root.left.value, 3)
    self.assertEqual(tree.root.right.value, 7)
    self.assertEqual(tree.root.left.left.value, 2)
    self.assertEqual(tree.root.left.right.value, 4)
    self.assertEqual(tree.root.right.left.value, 6)
    self.assertEqual(tree.root.right.right.value, 8)

  if __name__ == '--main--':
    unittest.main()