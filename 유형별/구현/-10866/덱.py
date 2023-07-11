n= int(input())
deck = []
from collections import deque
import sys
dq = deque()
for _ in range(n):
    word = sys.stdin.readline()
    if word[:9] == 'push_back':
        a = word.index(" ")
        t = word[a:]
        dq.append(int(t))
    elif word[:10] == 'push_front':
        a = word.index(" ")
        t = word[a:]
        dq.appendleft(int(t))
    elif word[:5] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif word[:4] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
    elif word[:4] == 'size':
        print(len(dq))
    elif word[:5] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif word[:9] == 'pop_front':
        if dq:
            a = dq.popleft()
            print(a)
        else:
            print(-1)
    elif word[:8] == 'pop_back':
        if dq:
            a = dq.pop()
            print(a)
        else:
            print(-1)


