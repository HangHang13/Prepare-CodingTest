N,M,K = map(int, input().split())
arr = [[0] * N for _ in range(M)]

st = []
for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    st.append([r,c,m,s,d])


#배열설정
for lst in st:
    r = lst[0]-1
    t = lst[1]-1
    arr[r][t] = lst[2]


