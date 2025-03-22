import sys
sys.stdin = open('input.txt','r')

sys.setrecursionlimit(10000)

def dfs(y,x):
    global gg
    if y<0 or y>n-1 or x<0 or x>n-1:
        return
    if arr[y][x] ==0:
        return
    for a in range(0, num)


n= int(input())
arr=[]

for i in range(n):
    arr.append(list(map(int, input().split())))

cnt=0
num=0
irland = [[] for _ in range(100000)]

minL = 10000

for y in range(n):
    for x in range(n):
        if arr[y][x] ==1:
            num+=1
            dfs(y,x)

