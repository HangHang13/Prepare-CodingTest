import sys
sys.stdin = open('input.txt','r')
n= int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))

print(arr)

t=[]
for a in range(n):
    t.append(arr[n][n])