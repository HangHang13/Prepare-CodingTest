import sys
import collections
sys.stdin = open('sample_input.txt')

#케이스입력
num = int(input())
#그래프 구성

for tc in range(1):
    # n=세로 m =가로 =>그래프 r=세로 c=가로 =>시작위치 ,l =시간
    n,m,r,c,l = map(int,input().split())

    arr= []
    graph = collections.defaultdict()
    for _ in range(n):
        arr.append(list(map(int, input().split())))


    for x in arr:
        for y in x:
            graph[y].append(x)

    print(f'#{tc} {n,m,r,c,l} {graph}')

