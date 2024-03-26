class HashTable:
  def __init__(self, capacity=10):
    self.capacity = capacity
    self.size = 0
    self.buckets = [[] for _ in range(capacity)]

  def hash(self, key):
    return hash(key) % self.capacity
  
  def insert(self, key, value):
    index = self.hash(key)
    bucket = self.buckets[index]
    for i, (k, v) in enumerate(bucket):
      if k == key:
        bucket[i] = (key, value)
        return
    bucket.append((key, value))
    self.size += 1

  def find(self, key):
    index = self.hash(key)
    bucket = self.buckets[index]
    for k, v in bucket:
      if k == key:
        return v
    return None
  
  def delete(self, key):
    index = self.hash(key)
    bucket = self.buckets[index]
    for i, (k, v) in enumerate(bucket):
      if k == key:
        del bucket[i]
        self.size -= 1
        return True
  
  def __str__(self):
    return "".join(f"{i}: {bucket}\n" for i, bucket in enumerate(self.buckets))