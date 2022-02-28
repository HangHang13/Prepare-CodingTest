import sys
sys.stdin = open('input.txt')

num = int(sys.stdin.readline())

di=[0,0,1,-1] #좌우 상하
dj=[1,-1,0,0]

for tc in range(1,num+1):

    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    # 8가지 방향을 담음
    delta = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
    n = N//2
    #2 = 백돌 , 1 = 흑돌
    board[n-1][n-1]=2
    board[n-1][n]=1
    board[n][n-1]=1
    board[n][n]=2
    for _ in range(M):
        x,y,z = map(int, input().split())
        y,x = y-1,x-1

        if not board[y][x]:
            board[y][x] = z
            for i in range(8):
                dx,dy = delta[i]
                nx, ny = x+dx, y+dy
                #뒤집을 좌표
                res = []
                while True:

                    if nx<0 or N-1<nx or ny<0 or N-1<ny:
                        break
                    #공백확인
                    if board[nx][ny] == 0:
                         break
                    #같은 색깔 멈춤
                    if board[nx][ny] == z:
                        break
                    else:

                    nx += dx
                    ny += dy


    W, B = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                W+=1
            elif board[i][j] ==2:
                B+=1
    print(f'#{tc} {W} {B}')



