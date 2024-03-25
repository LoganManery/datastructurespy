def create_node(value, next=None):
  return(value, next)

def append(head, value):
  if head is None:
    return create_node(value)
  else:
    return(head[0], append(head[1], value))
  
def prepend(head, value):
  return create_node(value, head)

def remove(head, value):
  if head is None:
    return None
  elif head[0] == value:
    return head[1]
  else:
    return(head[0], remove(head[1], value))
  
def find(head, value):
  if head is None:
    return False
  elif head[0] == value:
    return True
  else:
    return find(head[1], value)
  
def to_list(head):
  if head is None:
    return []
  else:
    return [head[0]] + to_list(head[1])