# checking whether the undirected graph is connected or not 

class Queue:
  def __init__(self):
    self.queue = []

  # isEmpty
  def isEmpty(self):
    if(self.queue == []):
      return True
    else:
      return False
  
  # enqueue
  def enqueue(self, v):
    self.queue.append(v)
  # dequeue
  def dequeue(self):
    v = None
    if(not self.isEmpty()):
      v = self.queue[0]
      self.queue = self.queue[1:]
    else:
      print("queue is empty ")
    return v
# even if the parent = -1 after this function for a particular vertex , then also we can consider the graph as disconnected :
# but we want to know the number of disconnected components 

def Components(Alist):
  Components = {}

  for i in Alist.keys():
    Components[i] = -1
  
  (compid, seen) = (0, 0)
  
  return None