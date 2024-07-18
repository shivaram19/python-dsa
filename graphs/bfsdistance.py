import random

class Queue:
  def __init__(self):
    self.queue = []
  
  def isEmpty(self):
    return(self.queue == [])
  
  def addq(self, v):
    self.queue.append(v)
  
  def delq(self):
    v = None
    if(self.isEmpty()):
      print("Queue is Empty")
    else:
      v = self.queue[0]
      self.queue = self.queue[1:]
    return(v)


def generate_random_adjacency_list(num_nodes, num_edges):
  adj_list = {i: [] for i in range(num_nodes)}
  
  all_possible_edges = [(i, j) for i in range(num_nodes) for j in range(i+1, num_nodes)]
  random.shuffle(all_possible_edges)
  
  edges = all_possible_edges[:num_edges]
  
  for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)
  return adj_list

list = generate_random_adjacency_list(5, 6)


def bfsOrder(AList, v):
  (level, parent) = ({}, {})

  for i in AList.keys():
    level[i] = 0;
    parent[i] = -1;

  q = Queue()

  level[v] = 0;
  q.addq(v)

  while(not q.isEmpty()):
    j = q.delq()

    for neighbour in AList[j]:
      if(level[neighbour] == 0):
        parent[neighbour] = j
        level[neighbour] = level[j] + 1
  
  return(level, parent)


hakuna = bfsOrder(list, 2)

print(hakuna)