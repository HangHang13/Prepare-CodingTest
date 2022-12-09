import sys
# input = sys.stdin.readline


def check():
    pass




n,m,h = map(int, input().split())
graph = [[0]*n for _ in range(h)]

for i in range(m):
    a,b=map(int, input().split())

    graph[a-1][b-1] = 1


for a in graph:
    for b in a:
        print(b, end=" ")
    print()

