class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def append(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.size += 1

  def prepend(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def delete(self, data):
    current = self.head
    while current:
      if current.data == data:
        if current.prev:
          current.prev.next = current.next
        if current.next:
          current.next.prev = current.prev
        if current == self.head:
          self.head = current.next
        if current == self.tail:
          self.tail = current.prev
        return
      current = current.next

  def display(self):
    elements = []
    current = self.head
    while current:
      elements.append(current.data)
      current = current.next
    print(elements)