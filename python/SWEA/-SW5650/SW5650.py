import sys
from pprint import pprint
from collections import deque
sys.stdin = open('input.txt')
#상우하좌
dy=[-1,0,1,0]
dx=[0,1,0,-1]
change= [[],

         ]


#a[:2]+ b + a[2:]
#대차도 가능
num = int(input())

for tc in range(1):
    n=int(input())

    arr=[]
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    print(arr)
    #print(f'#{tc} {result}')


