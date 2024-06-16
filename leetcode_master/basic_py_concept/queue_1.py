# Queues (double ended queue)

from collections import deque 

queue = deque()
queue.append(1)
queue.append(4)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(7)
print("appendleft",queue)

queue.pop()
print("pop",queue)

