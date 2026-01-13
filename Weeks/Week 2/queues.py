#Dequeue
from collections import deque
queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
queue.popleft()  # Removes 'A'
print("Queue after one dequeue:", queue)
print("Initial queue:", queue)  


#Tupules are deifined using parenthesis
point = 1, 2
point2 = () #Empty tuple
point3 = (1,) * 3 #Single item tuple

#convert list to tuple
point4 = tuple([1,2,3])
print(point[0:2])
print(point3)
print(type(point))