import sys
import collections
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for tc in range(1):
    k = int(input())
    lst1 = [collections.deque(map(int,input().split())) for _ in range(4)]
    print(lst1)
    for _ in range(k):
        n, d = map(int,input().split())
        move = ([n,d])
        print(move)
    '''
    
def rotate(index, d):
    if d == 1:
        gears[index].appendleft(gears[index].pop())
    elif d == -1:
        gears[index].append(gears[index].popleft())

for test_case in range(1):
    K = int(input())
    gears = [deque(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        n, d = map(int, input().split())
        n -= 1
        move = [(n, d)]
        print(move)
        temp = d
        for i in range(n - 1, -1, -1):
            if gears[i][2] != gears[i + 1][6]:
                temp *= -1
                move.append((i, temp))
            else:
                break

        temp = d
        for i in range(n + 1, 4):
            if gears[i][6] != gears[i - 1][2]:
                temp *= -1
                move.append((i, temp))
            else:
                break

        for idx, direction in move:
            rotate(idx, direction)

    answer = 0
    for i in range(4):
        if gears[i][0] == 1:
            answer += 2**i

    print(f"#{test_case} {answer}")    
    
    
    
    
    
    
    k = int(input())
    lst1 =collections.deque(list(map(int, input().split())))
    lst2 = collections.deque(list(map(int, input().split())))
    lst3 = collections.deque(list(map(int, input().split())))
    lst4 = collections.deque(list(map(int, input().split())))

    direction=[]
    for _ in range(k):
        direction.append(list(map(int,input().split())))
    print(direction)

    for a,b in direction:
        if a==1:
            lst1.rotate(b)
            if lst1[2] !=lst2[6]:
                while lst1[2]==lst2[6]:
                    lst2.rotate(-1)
                if lst2[2]!=lst3[6]:
                    while lst2[2]==lst3[6]:
                        lst3.rotate(1)
                    if lst3[2]!=lst4[6]:
                        while lst3[2]==lst4[6]:
                            lst4.rotate(-1)
        if a==2:
            lst2.rotate(b)
            if lst2[2] != lst3[6]:
                while lst2[2] == lst3[6]:
                    lst3.rotate(-1)
                if lst3[2] != lst4[6]:
                    while lst3[2] == lst4[6]:
                        lst4.rotate(1)
                    if lst1[2] != lst2[6]:
                        while lst1[2] == lst2[6]:
                            lst1.rotate(-1)

        if a==3:
            lst3.rotate(b)
            if lst3[2] !=lst4[6]:
                while lst3[2]==lst4[6]:
                    lst4.rotate(-1)
                if lst2[2]!=lst3[6]:
                    while lst2[2]==lst3[6]:
                        lst2.rotate(-1)
                    if lst1[2]!=lst2[6]:
                        while lst1[2]==lst2[6]:
                            lst1.rotate(1)

        if a==4:
            lst4.rotate(b)
            if lst3[2] != lst4[6]:
                while lst3[2] == lst4[6]:
                    lst3.rotate(-1)
                if lst2[2] != lst3[6]:
                    while lst2[2] == lst3[6]:
                        lst2.rotate(1)
                    if lst1[2] != lst2[6]:
                        while lst1[2] == lst2[6]:
                            lst1.rotate(-1)

    res=0
    print(f'lst1{lst1}')
    print(f'lst2{lst2}')
    print(f'lst3{lst3}')
    print(f'lst4{lst4}')
    if lst1[0] == 0:
        res+=0
    else:
        res+=1
    if lst2[0]==0:
        res+=0
    else:
        res+=2
    if lst3[0]==0:
        res+=0
    else:
        res+=4
    if lst4[0]==0:
        res+=0
    else:
        res+=8

    print(f'#{tc} {res}')
'''