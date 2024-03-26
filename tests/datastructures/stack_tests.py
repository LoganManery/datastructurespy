import unittest

from datastructures.stack import Stack

class TestStack(unittest.TestCase):
  def test_is_empty(self):
    stack = Stack()
    self.assertTrue(stack.isEmpty())
  
  def test_push(self):
    stack = Stack()
    stack.push(1)
    self.assertFalse(stack.isEmpty())

  def test_pop(self):
    stack = Stack()
    stack.push(1)
    stack.push(2)
    removed = stack.pop()
    self.assertEqual(removed, 2)
    self.assertEqual(stack.size(), 1)

  def test_peek(self):
    stack = Stack()
    stack.push(1)
    stack.push(2)
    self.assertEqual(stack.peek(), 2)

  def test_size(self):
    stack = Stack()
    for i in range(5):
      stack.push(i)
    self.assertEqual(stack.size(), 5)

  def test_pop_empty(self):
    stack = Stack()
    with self.assertRaises(Exception) as context:
      stack.pop()
    self.assertTrue('Pop from an empty stack' in str(context.exception))

  def test_peek_empty(self):
    stack = Stack()
    with self.assertRaises(Exception) as context:
      stack.peek()
    self.assertTrue('Peek from an empty stack' in str(context.exception))

if __name__ == '__main__':
  unittest.main()