from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a,b = map(int, input().split())
    q = deque()
    q.append((a,""))
    visit = [False] * 10000

    while q:
        num ,path = q.popleft()
        visit[num] = True
        if num == b:
            print(path)
            break
        
        num2 = (2*num)% 10000
        if not visit[num2]:
            q.append((num2, path+"D"))
            visit[num2] = True

        num2 = (num-1)% 10000
        if not visit[num2]:
            q.append((num2, path+"S"))
            visit[num2] = True

        num2 = (10*num+(num//1000))%10000
        if not visit[num2]:
            q.append((num2, path+"L"))
            visit[num2] = True
        
        num2 = (num//10 + (num%10)*1000)%10000
        if not visit[num2]:
            q.append((num2, path+"R"))
            visit[num2] = True


