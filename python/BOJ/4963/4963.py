
def DFS(i,j):
    if i<0 or i>=h or j<0 or j>=w or arr[i][j] != 1:
        return

    arr[i][j] = 0

    DFS(i+1,j)
    DFS(i-1,j)
    DFS(i,j+1)
    DFS(i,j-1)

    DFS(i+1, j+1)
    DFS(i-1,j-1)
    DFS(i-1,j+1)
    DFS(i+1,j-1)
    


while True:
    w,h = map(int,input().split())
    if w ==0 and h ==0:
        break
    arr = []
    
    for _ in range(h):
        arr.append(list(map(int,input().split())))
    cnt=0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                DFS(i,j)
                cnt+=1

    print(cnt)
