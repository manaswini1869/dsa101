# Add any extra import statements you may need here


# Add any helper functions you may need here

class Node:
    def __init__(self, key=None, value=None):
      self.key = key
      self.value = value
      self.next = None
      self.prev = None

class LRUCache:

  def __init__(self, capacity):
    # Write your code here
    self.capacity = capacity
    self.cache = {}
    self.head = Node()
    self.tail = Node()
    self.head.next = self.tail
    self.tail.prev = self.head

  def addNode(self, node):
    node.prev = self.head
    node.next = self.head.next
    self.head.next.prev = node
    self.head.next = node

  def deleteNode(self, node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node

  def movetohead(self, node):
    self.deleteNode(node)
    self.addNode(node)

  def poptail(self):
    tail_node = self.tail.prev
    self.deleteNode(tail_node)
    return tail_node

  def get(self, key):
    if key in self.cache:
      node = self.cache[key]
      self.movetohead(node)
      return node.value
    return -1

  def set(self, key, value):
    if key in self.cache:
      node = self.cache[key]
      node.value = value
      self.movetohead(node)
    else:
      if len(self.cache) >= self.capacity:
        tail_node = self.poptail()
        del self.cache[tail_node.key]
      new_node = Node(key, value)
      self.addNode(new_node)
      self.cache[key] = new_node

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":
  cacheOne = LRUCache(2)
  cacheOne.set(1, 2)
  outputOne = [cacheOne.get(1)]
  check([2], outputOne)

  cacheTwo = LRUCache(2)
  cacheTwo.set(1,2)
  cacheTwo.set(2,3)
  cacheTwo.set(1,5)
  cacheTwo.set(4,5)
  cacheTwo.set(6,7)
  outputTwo = [cacheTwo.get(4)]
  cacheTwo.set(1,2)
  outputTwo.append(cacheTwo.get(3))
  check([5, -1], outputTwo)

  # Add your own test cases here

