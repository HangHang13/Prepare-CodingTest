import sys
from queue import Queue
sys.stdin = open('input.txt')





for tc in range(1):
    # 테스트케이스 T, 번호길이의 총갯수 K
    T = map(int, input().split())
               
    #입력 리스트
    lst = list(map(int, input().split()))
    
    que = Queue()
    for x in lst:
        que.put(x)
    lst2=[]
    i=0
    while 1:
        for k in range(1,5):
            item = que.get()
            kk = item - k
            que.put(kk)
            print(que.queue)
            # print(kk)
            # print(que.queue)
            if kk<0:
                break
        if kk==0:
            print(que.queue)
            break


    a = que
    # b = a-1
    # print(f'#{tc} {a}')

