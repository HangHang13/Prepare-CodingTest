
import sys
input = sys.stdin.readline


n = int(input())

arr = []
dy = [1,0,-1,0]
dx = [0,-1,0,1] #북서 동남
for _ in range(n):
    pos_x = 0
    pos_y = 0
    pos_dir = 0
    road  = list(input())
    min_x, min_y, max_x,max_y =0,0,0,0
    for i in road:
        if i == 'F':
            pos_x = pos_x+dx[pos_dir]
            pos_y = pos_y+dy[pos_dir]
        elif i == 'B':
            pos_x = pos_x-dx[pos_dir]
            pos_y = pos_y-dy[pos_dir]
        elif i== 'L':
            if pos_dir == 3:
                pos_dir = 0
            else:
                pos_dir +=1
        elif i =='R':
            if pos_dir == 0:
                pos_dir =3
            else:
                pos_dir-=1
        min_x = min(pos_x, min_x)
        min_y = min(pos_y, min_y)
        max_y = max(pos_y, max_y)
        max_x = max(pos_x, max_x)


    print(abs(max_x-min_x)*abs(max_y-min_y))

