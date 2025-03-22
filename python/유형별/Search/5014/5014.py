import sys
import collections
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())



def bfs():
    q = collections.deque([S])
    vis = [0] * (F + 1)
    vis[S] = 1
    while q:
        a = q.popleft()

        if a == G:
            print(vis[a]-1)
            return
        if a + U <= F and vis[a+U]==0:
            q.append(a + U)
            vis[a+U] = vis[a] + 1
        if 1 <= a - D and vis[a-D]==0:
            q.append(a - D)
            vis[a - D] = vis[a] + 1
    else:
        print('use the stairs')
        return

bfs()
