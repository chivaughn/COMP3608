'''
Full Name: Chivaughn Charles
Student ID: 815007458
Email: chivaughncharles@gmail.com
Course Code: COMP 3608
'''

import collections
INPUT_FILEPATH = 'edgelist.txt'
DELIMITER = ','

from queue import PriorityQueue

def neighbors(node,edges):
        return edges[node]

def get_cost(from_node, to_node,costs):
    return costs[(from_node + to_node)]

    
def ucs(edges,cost,start,goal):
  closed = []
  open = PriorityQueue()
  open.put((0, start,start))
  while open:
    print(closed)
    print(open.queue,'\n')
    cost, node, path = open.get()
    if node not in closed:
      closed.append(node)
      if node == goal:
        break
      if node in edges:
        for i in neighbors(node,edges):
          if i not in closed:
              total_cost = cost + get_cost(node, i,costs)
              open.put((total_cost, i, path+i))
  print(closed)
  print(open.queue,'\n')
  print('path: ', path)
  print('cost: ', cost)
  



edges = {  
}

costs = {
}


with open(INPUT_FILEPATH, 'r',encoding='utf-8-sig') as fp:
    for line in fp:
        contents = line.split(DELIMITER)
        cost = 1
        u = (contents[0])
        v = (contents[1])
        if len(contents) > 2:
            cost = int(contents[2])
        if u in edges:
          edges[u] += v
        else:
          edges[u] = [v]
        costs[(u+v)] = cost
        costs[(v+u)] = cost


ucs(edges,costs,'a','m')
