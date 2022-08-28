import sys
input = sys.stdin.readline

#n 세로 m 가로 r 회전수
n,m,r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
short = n if n<= m else m



