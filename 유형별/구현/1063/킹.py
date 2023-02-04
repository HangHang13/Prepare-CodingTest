a, b, n = input().split()

chess = [[0] * 8 for _ in range(8)]

# 좌우상하오른위대각왼쪽위대각
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]


y=0
x=0

a=list(a)
b=list(b)
