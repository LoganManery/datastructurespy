class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, value):
    if self.head is None:
      self.head = Node(value)
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = Node(value)

    def prepend(self, value):
      new_head = Node(value)
      new_head.next = self.head
      self.head = new_head

    def delete(self, value):
      current = self.head
      if current and current.value == value:
        self.head = current.next
        return
      
      prev = None
      while current and current.value != value:
        prev = current
        current = current.next

      if current:
        prev.next = current.next

    def find(self, value):
      current = self.head
      while current:
        if current.value == value:
          return current
        current = current.next
      return None
    
    def display(self):
      elements = []
      current = self.head
      while current:
        elements.append(current.value)
        current = current.next
      return elements

      