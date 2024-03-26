class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.size = 0

  def isEmpty(self):
    return self.size == 0
  
  def enqueue(self, value):
    newNode = Node(value)
    if self.rear is None:
      self.front = self.rear = newNode
    else:
      self.rear.next = newNode
      self.rear = newNode
    self.size += 1

  def dequeue(self):
    if self.isEmpty():
      raise Exception("dequeue from an empty queue")
    removed = self.front
    self.front = self.front.next
    if self.front is None:
      self.rear = None
    self.size -= 1
    return removed.value
  
  def peek(self):
    return self.size