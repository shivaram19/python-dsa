import random 

class Queue:
  def __init__(self):
    self.queue = []

  def isEmpty(self):
    if(self.queue == []):
      return True
    else:
      return False

  def addq(self, v):
    self.queue.append(v)

  def delq(self):
    v = None
    if(self.isEmpty()):
      print("Queue is Empty")
    else:
      v = self.queue[0]
      self.queue = self.queue[1:]
    return v


  
def generate_random_adjacency_list(num_nodes, num_edges):
  adj_list = {i: [] for i in range(num_nodes)}
  
  all_possible_edges = [(i, j) for i in range(num_nodes) for j in range(i+1, num_nodes)]
  random.shuffle(all_possible_edges)
  
  edges = all_possible_edges[:num_edges]
  
  for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)
  return adj_list
        



def BFS_LIST(AList, v):
  (visited,parent) = ({}, {})
  for i in AList.keys():
    visited[i] = False
    parent[i] = -1
  
  visited[v] = True
  q = Queue()
  q.addq(v)

  while(not q.isEmpty()):
    j = q.delq()
    for i in (AList[j]):
      if(not visited[i]):
        visited[i] = True
        parent[i] = j
        q.addq(i)
  return (visited, parent)
  

random_adj_list = generate_random_adjacency_list(5, 6)
hakuna = BFS_LIST(random_adj_list, 0)
print(hakuna)