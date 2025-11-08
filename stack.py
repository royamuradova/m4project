class Stack:
  """Adapter over Python list exposing ONLY stack ops (LIFO)."""

  def __init__(self):
      self._data = []

  def push(self, item):
      self._data.append(item)

  def pop(self):
      if self.is_empty():
          raise IndexError("pop from empty stack")
      return self._data.pop()

  def peek(self):
      if self.is_empty():
          raise IndexError("peek on empty stack")
      return self._data[-1]

  def is_empty(self):
      return len(self._data) == 0

  def size(self):
      return len(self._data)

  def __repr__(self):
      return f"Stack(top->bottom: {list(reversed(self._data))})"
