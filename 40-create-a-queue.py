#using a list as a queue FIFO->First in, first out
queue = []
queue.append('data 1')
queue.append('data 2')
print(queue)
queue.pop()
print(queue)
queue.append('data 2')
queue.pop(0) #stack structure
print(queue)