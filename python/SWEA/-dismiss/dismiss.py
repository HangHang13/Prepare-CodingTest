import sys
import collections
sys.stdin = open('sample_input (1).txt')




dy=[-1,1,0,0]
dx=[0,0,-1,1]

T = int(input())

for test_case in range(1):
    tc= int(input())
    atmos=[]
    for a in range(tc):
        x,y,d,k = map(int,input().split())


        atmos.append([x,y,d,k])
    cnt=0
    energy=0
    while 1:
        dic={}
        for a in atmos:
    print(f'#{test_case} ')
