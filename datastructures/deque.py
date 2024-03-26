class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None
    self.prev = None

class Deque:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def isEmpty(self):
    return self.head is None
  
  def append(self, data):
    new_node = Node(data)
    if self.isEmpty():
      self.haed = self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.size += 1

  def appendleft(self, data):
    new_node = Node(data)
    if self.isEmpty():
      self.head = self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.size += 1

  def pop(self):
    if self.isEmpty():
      raise IndexError("Pop from an empty deque")
    data = self.tail.data
    if self.head == self.tail:
      self.head = self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
    self.size -= 1
    return data
  
  def popleft(self):
    if self.isEmpty():
      raise IndexError("Pop from an empty deque")
    data = self.head.data
    if self.head == self.tail:
      self.head = self.tail = None
    else:
      self.head = self.head.next
      self.head.prev = None
    self.size -= 1
    return data
  
  def peek(self):
    if self.isEmpty():
      raise IndexError("Peek from an empty deque")
    return self.tail.data
  
  def peekleft(self):
    if self.isEmpty():
      raise IndexError("Peek from an empty deque")
    return self.head.data
  
  def getSize(self):
    return self.size