'''
Full Name: Chivaughn Charles
Student ID: 815007458
Email: chivaughncharles@gmail.com
Course Code: COMP 3608
'''

from collections import defaultdict
from queue import PriorityQueue

INPUT_FILE = 'maze.txt'

G = defaultdict(lambda: defaultdict(dict))
h = {}


fp = open(INPUT_FILE, 'r')
data = fp.read()
fp.close()

data = data.split('\n')

def is_valid_coord(t, n):
    x = t[0]
    y = t[1]
    test1 = x >= 0
    test2 = x < n
    test3 = y >= 0
    test4 = y < n
    return (test1 and test2 and test3 and test4)

n = len(data)
END_X = 5
END_Y = 5
for i in range(n):
    for j in range(n):
        if data[i][j] != 'X':
            coords = [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]
            coords = list(filter(lambda x: is_valid_coord(x, n), coords))
            for x,y in coords:
                if data[x][y] != 'X':
                    G[(i+1,j+1)][(x+1,y+1)]['cost'] = 1
            h[(i+1,j+1)] = abs(i+1 - END_X) + abs(j+1 - END_Y)

G = dict(G)
G = {k:dict(v) for k, v in G.items()}

def neighbors(node,G):
        return G[node]

def get_cost(x,h):
    return h[x]


def bestfs (G,h,start,goal):
    open = PriorityQueue()
    open.put((h[start], start,start))
    closed = []
    path = []
    while open:
        print(closed)
        print(open.queue,'\n')
        cost, node, path = open.get()
        if node not in closed:
            closed.append(node)
        if node == goal:
            break
        if node in G:
            for i in neighbors(node,G):
                if i not in closed:
                    total_cost = get_cost(node,h)
                    open.put((total_cost, i, path+i))
    index = 0
    print('path: ', end='')
    for x in path:
        if index is 0:
            print('(',end='')
        index += 1
        if index is 1:
            print(x,end=' ')
        elif index is 2:
            print(x,end=')')
            index = 0

bestfs(G,h,(1,1),(5,5))
