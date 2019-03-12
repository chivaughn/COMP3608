'''
Full Name: Chivaughn Charles
Student ID: 815007458
Email: chivaughncharles@gmail.com
Course Code: COMP 3608
'''

def dfs(graph,start,goal):
  open = [start]
  closed = []
  temp = []
  while open:
    print(open)
    print(closed)
    print('\n')
    vertex = open.pop(0)
    if vertex in closed:
      continue
    closed.insert(0,vertex)
    if vertex is goal:
      break
    if vertex in graph:
      for neighbor in graph[vertex]:
        temp.append(neighbor)
      temp.reverse()
      for num in temp:
        open.insert(0,num)
      temp.clear()
  print(open)
  print(closed)
  closed.reverse()
  print('path: ', end = '')
  for vertex in closed:
    print(vertex, end = ' ')


graph1 = {}

import collections

INPUT_FILEPATH = 'edgelist.txt'
DELIMITER = ','

with open(INPUT_FILEPATH, 'r',encoding='utf-8-sig') as fp:
    for line in fp:
        contents = line.split(DELIMITER)
        cost = 1
        u = (contents[0])
        v = (contents[1])
        if len(contents) > 2:
            cost = float(contents[2])
        if u in graph1:
          graph1[u] += v
        else:
          graph1[u] = [v]

#print(graph1)
dfs(graph1,'a','m')