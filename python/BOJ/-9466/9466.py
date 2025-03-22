import sys
import collections


n=int(input())


def DFS(tmp):
    vis.append(tmp)
    for node in graph[tmp]:
        if node == tmp :
            king.append(node)
            return
        else:
            DFS(tmp)

for _ in range(1):
    k = int(input())
    arr  = [0] * k
    lst= collections.deque()
    graph = collections.defaultdict(list)
    grid = list(map(int, input().split()))
    # graph = defaultdict(list)
    # for i in range(0, len(lst), 2):
    #     a = lst[i]
    #     b = lst[i+1]
    
    
        
    #     grid[a][b] = 1
    #     grid[b][a] = 1
    
    #     graph[a].append(b)
    #     graph[b].append(a)
    for a,b in enumerate(grid, start=1):
        lst.append((a,b))

    print(lst)

    while lst:
        i,j = lst.popleft()

        graph[i].append(j)
        #graph[j].append(i)

    print(graph)
    stack = []
    vis=[]
    king = []
    stack.append(1)
    vis.append(1)
    cnt=0
    for i in range(1,k):
        DFS(i)
    print(vis)