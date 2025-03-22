import sys
import collections
sys.stdin = open('input.txt')

dy=[1,-1,0,0]
dx=[0,0,1,-1]
def bfs():
    q=collections.deque()
    q.append((0,0))
    vis[0][0]=1
    cnt=0
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<n and 0<=nx<m and vis[ny][nx]==0:
                if arr[ny][nx]==0:
                    vis[ny][nx]=1
                    q.append((ny,nx))
                elif arr[ny][nx]==1:
                    arr[ny][nx]=0
                    vis[ny][nx]=1
                    cnt+=1
    ko.append(cnt)
    return cnt


n , m = map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))

ko=[]

time=0
while 1:
    time +=1
    vis = [[0] * m for _ in range(n)]
    cnt = bfs()
    if cnt==0:
        time-=1
        break

print(time)
print(ko[-2])

# for a in arr:
#     for b in a:
#         print(b, end=" ")
#     print()