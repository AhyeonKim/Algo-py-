import heapq
def find():

def union():

V,E = map(int,input().split())
nodes = [[] for _ in range(V)]
for _ in range(E):
    s,e,w = map(int,input().split())
    nodes[s].append((e,w))