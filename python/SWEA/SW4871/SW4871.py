import sys
sys.stdin = open('input.txt')





for tc in range(1,11):
    # 테스트케이스 T, 번호길이의 총갯수 K
    T, K = map(int, input().split())
               
    #입력 리스트
    lst = list(map(int, input().split()))
    
    #graph 생성
    arr = {}

    for i in range(0,K*2,2):
        v = lst[i]
        a = lst[i+1]
        arr[v] = arr.get(v, []) + [a]

    stack = []
    stack.append(0)
    visit = [0] *100
    while stack:
        x = stack.pop()
        visit[x]=1
        if x in arr.keys():
            for a in arr[x]:
                stack.append(a)

    print(f'#{tc} {visit[-1]}')

