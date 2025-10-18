class my_queue():
 def __init__(self, capacity):
    self.my_array =  [0] * capacity
    self.size = 0
    self.capacity = capacity

 def enqueue(self, value) :
   if self.size  == self.capacity:
     print("array is full")
   self.my_array[self.size] = value
   self.size += 1

 def dequeue(self):
   print(self.my_array[0])

   for i in range(1, self.size):
            self.my_array[i - 1] = self.my_array[i]

   self.size -= 1
   pass
   
queue =  my_queue(4)
queue.enqueue(40)
queue.enqueue(30)
queue.enqueue(20)
queue.enqueue(10)

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()


     
     