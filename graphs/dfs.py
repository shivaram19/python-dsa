import random



class Stack:
  def __init__(self):
    self.stack = [0]
    self.top = 0

  def isEmpty(self):
    if(self.stack == [0]):
      return True
    else:
      return False
  
  def push(self, v):
    self.top = self.top+1 
    self.stack.append(v)

  def pop(self):
    if(self.isEmpty()):
      return 0;
    else:
      v = self.stack[self.top]
      self.top = self.top - 1
      self.stack = self.stack[:self.top+1]
      return v;


def generate_connected_graph(n):
  if n <= 1:
    return {0: []}
  
  # Step 1: Create a list of nodes
  nodes = list(range(n))
  
  # Step 2: Create an empty adjacency list
  adj_list = {i: [] for i in nodes}
  
  # Step 3: Ensure the graph is connected by creating a spanning tree
  # Pick a random starting node
  random.shuffle(nodes)
  for i in range(n - 1):
    adj_list[nodes[i]].append(nodes[i + 1])
    adj_list[nodes[i + 1]].append(nodes[i])
  
  # Step 4: Add random edges
  edge_count = random.randint(n, 2 * n)  # Number of edges can vary
  for _ in range(edge_count):
    u, v = random.sample(nodes, 2)
    if v not in adj_list[u]:
      adj_list[u].append(v)
      adj_list[v].append(u)
  
  return adj_list

# Example usage:
n = 5  # Number of nodes
adj_list = generate_connected_graph(n)
print(adj_list)

def dfs(Alist, v):
  visited = {}
  for i in Alist.keys():
    visited[i] = False
  
  s = Stack()

  visited[v] = True
  s.push(v)
  while( not s.isEmpty()):
    x = s.pop()
    for neighbours in Alist[x]:
      if(not visited[neighbours]):
        visited[neighbours] = True
        s.push(neighbours)
  return(visited)


defi = dfs(adj_list, 4)

print(defi)

# arr = [1, 3, 4, 5 ,6, 7, 8, 9 ,0]

# arr = arr[1:]
# print(arr) 

# # [ 3, 4, 5 ,6, 7, 8, 9 ,0]

# arr = arr[:7]

# print(arr)
# # [ 3, 4, 5 ,6, 7, 8, 9 ]

# arr = arr[0:6]

# print(arr)