# πSWEA4615 μ¬λ―Έμλ μ€μλ‘

## πΊνμν κ°λ

- μ’νμν, λ€μ§μ΄μ£Όλκ² κ΅¬ν, whileλ¬Έ νμ©, λΈννμ

## πΊνμ΄κ³Όμ 

- μ²μμ κ³ μ λμ΄μλ λ°±λ,νλ μ€μ 

- λΈν νμμΌλ‘ μ‘°κ±΄μ κ΅¬λΆ

  

- ν ν, λ€μ§μ΄μ£Όλ λ°°μ΄μ λ°λ‘ μ μ₯νλ€μ whileλ¬Έμ΄ λλ λ λ€μ§μ΄μ£Όλκ±Έ μ€ννλ€.

- λ§μ§λ§μ λ°±λ,νλ κ²μ

## πΊμ½λ

```python
num = int(sys.stdin.readline())

for tc in range(1,num+1):

    N, M = map(int, input().split())
    #λΉ λ°°μ΄ λ°λν μμ±
    board = [[0]*N for _ in range(N)]
    # 8κ°μ§ λ°©ν₯μ νμ μ,ν,μ’,μ°,μ°μ’,μ°μ,μ’ν,μ’μ
    delta = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
    n = N//2
    #μ΄κΈ°κ° μ€μ 
    #2 = λ°±λ , 1 = νλ
    board[n-1][n-1]=2
    board[n-1][n]=1
    board[n][n-1]=1
    board[n][n]=2
    
    for _ in range(M):
        x,y,z = map(int, input().split())
        y,x = y-1,x-1
        board[x][y] =z
        
        # λ€μ§μ μ’ν λ¦¬μ€νΈ
        res = []
        for i in range(8):
            #[(1, 0), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, -1), (-1, 1)]
            dx,dy = delta[i]
            nx, ny = x+dx, y+dy

            while True:
                #λ²μ λ²μ΄λλ©΄ λ©μΆ€
                if nx<0 or N-1<nx or ny<0 or N-1<ny:
                    res=[]
                    break
                #κ³΅λ°±νμΈμ λ©μΆ€
                if board[nx][ny] == 0:
                    res = []
                    break
                #κ°μ μκΉ λ©μΆ€
                if board[nx][ny] == z:
                    break
                else:
                    res.append((nx,ny))
            	nx, ny = nx+dx, ny+dy
            
            for rx,ry in res:
                if z==1:
                    board[rx][ry]=1
                else:
                    board[rx][ry]=2
        
     
	#λ°±λ,νλ νμ
    W, B = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                W+=1
            elif board[i][j] ==2:
                B+=1
    
    print(f'#{tc} {W} {B}')

```

