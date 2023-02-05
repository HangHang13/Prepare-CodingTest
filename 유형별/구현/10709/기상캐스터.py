
h ,w =map(int, input().split())

arr = []

grd = [[-1] * w for _ in range(h)]

for _ in range(h):
    arr.append(input().rstrip())

for i in range(h):
    for j in range(w):
        if arr[i][j] == '.':
            continue
        else:
            grd[i][j] = 0
            for k in range(j+1, w):
                grd[i][k] = grd[i][k-1] + 1
                # if arr[i][k] == 'c':
                #     break

for a in grd:
    for b in a:
        print(b, end=" ")
    print()
