import sys
sys.stdin = open('input.txt')

num = int(sys.stdin.readline())

for tc in range(1,num+1):

    N, M = map(int, input().split())
    #빈 배열 바둑판 생성
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
        board[y][x] = z
        # 뒤집을 좌표
        res = []
        for i in range(8):
            dx, dy = delta[i]
            for k in range(N):
                #[(1, 0), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
                nx, ny = x+dx*k, y+dy*k
                #범위안에
                if 0<=nx<N and 0<=ny<N:
                    if board[ny][nx]==0:
                        print('kkk')
                        break
                    elif board[ny][nx]==z:
                        for cy,cx in res:
                            board[cy][cx]=z
                        break
                    else:
                        res.append((ny,nx))
                        print('lll')
                else:
                    break

        # for x in board:
        #     for y in x:
        #         print(y, end=" ")
        #     print()
        # print()

    W, B = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                W+=1
            elif board[i][j] ==2:
                B+=1
    print(f'#{tc} {W} {B}')



