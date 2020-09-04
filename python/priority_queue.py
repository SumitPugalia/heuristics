import heapq
from queue import PriorityQueue
import heapdict
from queue import Queue
from collections import deque 
  
# Initializing a queue 
q = Queue(maxsize = 3) 

l = [10, 5, 35, 25]
heapq.heapify(l)
print(heapq.heappop(l))
print(heapq.nlargest(2, l))

p = [("abc", 2), ("rcd", 4), ("cdf", 3)]
heapq.heapify(p)
print(list(p))

q = PriorityQueue()
q.put((5, "a"))
q.put((6, "b"))
q.put((3, "d"))
q.put((8, "d"))
q.put((3, "c"))

# remove and return  
# lowest priority item 
print(q.get())

  
h = heapdict.heapdict()
# Adding pairs into heapdict 
h['g']= 2
h['e']= 1
h['k']= 3
h['s']= 4
  
print('list of key:value pairs in h:\n',  
      list(h.items())) 
print('pair with lowest priority:\n', 
      h.peekitem()) 
print('list of keys in h:\n', 
      list(h.keys())) 
print('list of values in h:\n', 
      list(h.values())) 
print('remove pair with lowest priority:\n', 
      h.popitem()) 
print('get value for key 5 in h:\n', 
      h.get(5, 'Not found')) 
  
# clear heapdict h 
h.clear() 
print(list(h.items()))

