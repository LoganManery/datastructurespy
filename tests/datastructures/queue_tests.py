import unittest

from datastructures.queue import Queue

class TestQueue(unittest.TestCase):
  def test_enqueue(self):
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    self.assertEqual(queue.size, 3)
  
  def test_dequeue(self):
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    self.assertEqual(queue.dequeue(), 1)
    self.assertEqual(queue.dequeue(), 2)
    self.assertEqual(queue.dequeue(), 3)
    self.assertEqual(queue.size, 0)

  def test_peek(self):
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    self.assertEqual(queue.peek(), 3)
    queue.dequeue()
    self.assertEqual(queue.peek(), 2)
    queue.dequeue()
    self.assertEqual(queue.peek(), 1)
    queue.dequeue()
    self.assertEqual(queue.peek(), 0)