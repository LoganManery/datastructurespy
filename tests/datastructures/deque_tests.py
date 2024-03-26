import unittest

from datastructures.deque import Deque

class TestDeque(unittest.TestCase):
  def test_append(self):
    deque = Deque()
    deque.append(1)
    deque.append(2)
    deque.append(3)
    self.assertEqual(deque.size, 3)
  
  def test_appendleft(self):
    deque = Deque()
    deque.appendleft(1)
    deque.appendleft(2)
    deque.appendleft(3)
    self.assertEqual(deque.size, 3)
  
  def test_pop(self):
    deque = Deque()
    deque.append(1)
    deque.append(2)
    deque.append(3)
    self.assertEqual(deque.pop(), 3)
    self.assertEqual(deque.pop(), 2)
    self.assertEqual(deque.pop(), 1)
    self.assertEqual(deque.size, 0)
  
  def test_popleft(self):
    deque = Deque()
    deque.append(1)
    deque.append(2)
    deque.append(3)
    self.assertEqual(deque.popleft(), 1)
    self.assertEqual(deque.popleft(), 2)
    self.assertEqual(deque.popleft(), 3)
    self.assertEqual(deque.size, 0)
  
  def test_peek(self):
    deque = Deque()
    deque.append(1)
    deque.append(2)
    deque.append(3)
    self.assertEqual(deque.peek(), 3)
    deque.pop()
    self.assertEqual(deque.peek(), 2)
    deque.pop()
    self.assertEqual(deque.peek(), 1)
    deque.pop()
    self.assertEqual(deque.peek(), 0)