"""
In Python, append and pop operations on the beginning
or the left side of list objects are inefficient, with
O(n) time complexity. 

These operations are especially expensive if you're 
working with large lists because Python has to 
move all the items to the right to insert new items 
at the beginning of the list.

Python's deque was created to overcome this problem. 
Append and pop operations on both sides of a deque object 
are stable and equally efficient because deques are implemented 
as a doubly linked list. That's why deques are particularly useful 
for creating stacks and queues.
"""

import numbers
from collections import deque

# Empty deque obj
ticket_queue = deque()
print("ticket_queue:", ticket_queue)

# Peopel arrive to the queue
ticket_queue.append("Jane")
ticket_queue.append("John")
ticket_queue.append("Linda")
print("ticket_queue:", ticket_queue)

# People bought their tickets
print(ticket_queue.popleft())
print(ticket_queue.popleft())
print(ticket_queue.popleft())

# No people on the queue
# ticket_queue.popleft()

recent_files = deque(["core.py", "README.md", "__init__.py"], maxlen=3)
print(recent_files)

recent_files.appendleft("database.py")
print(recent_files)

recent_files.appendleft("requirements.txt")
print(recent_files)

# use different iterables to create deques
print(deque((1, 2, 3, 4)))

print(deque([1, 2, 3, 4]))

print(deque("abcd"))

# Unlike lists, deque doesn't support .pop() with arbitrary indices
# deque("abcd").pop(2)

# Extend an existing deque
numbers = deque([1, 2])
numbers.extend([3, 4, 5])
print(numbers)

numbers.extendleft([-1, -2, -3, -4, -5])
print(numbers)

# Insert an item at a given position
numbers.insert(5, 0)
print(numbers)