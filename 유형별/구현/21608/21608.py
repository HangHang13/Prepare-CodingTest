import sys
import collections

sys.stdin = open('input.txt', 'r')
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
q = collections.deque()
n = int(input())
arr = []
dict = collections.defaultdict(list)
for _ in range(n*n):
    a = list(map(int, input().rstrip().split()))
    std = a[0]
    like = a[1:]
    dict[std] = like
print(dict)

vis = [[0] * n for _ in range(n)]


for student, like in dict.items():
    tmp = []
    for y in range(n):
        for x in range(n):
            empty = 0
            cnt = 0
            if vis[y][x] !=0:
                continue
            for k in range(4):
                ny = y +dy[k]
                nx = x +dx[k]
                if ny<0 or ny>=n or nx<0 or nx>=n:
                    continue
                if vis[ny][nx] ==0:
                    empty+=1
                if vis[ny][nx] in like:
                    cnt+=1
            tmp.append([cnt,empty, y, x])

print(tmp)