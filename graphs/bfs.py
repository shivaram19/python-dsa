import random


class Queue:
  def __init__(self):
    self.queue = []

  def addq(self, v):
    self.queue.append(v)

  def isEmpty(self):
    if(self.queue == []):
      return True
    else:
      return False

  def delq(self):
    v = None
    if(self.isEmpty()):
      print("queue is empty")
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

# Example usage
num_nodes = 5
num_edges = 6
random_adj_list = generate_random_adjacency_list(num_nodes, num_edges)


def BFS_LIST(random_adj_list, v):

  visited = {}
  for i in (random_adj_list.keys()):
    visited[i] = False

  q = Queue()

  visited[v] = True
  q.addq(v)

  while(not q.isEmpty()):
    j = q.delq()
  for neighbours in (random_adj_list[j]):
    if(visited[neighbours] != True):
      visited[neighbours] = True
      q.addq(neighbours)
    
  return (visited)
  # return None

visited_nodes = BFS_LIST(random_adj_list,0)

print(visited_nodes)