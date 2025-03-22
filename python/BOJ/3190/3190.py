import sys
import collections
sys.stdin = open('input.txt')

n = int(input())


arr = [[0]* n for _ in range(n)]


apple = int(input())

for _ in range(apple):
    y, x = map(int, input().split())
    y-=1
    x-=1
    arr[y][x] = 2

snake =int(input())
q = collections.deque()
t =collections.defaultdict()
q.append((0,0))

for _ in range(snake):
    y, x = input().split()
    y= int(y)
    t[y]=x

#처음에 오른쪽을 향함
dy = [0,1,0,-1]
dx = [1,0,-1,0]
y,x = 0,0
arr[y][x] =1
cnt =0
d=0

def turn(a):
    global d
    if a=='L': #L은 왼쪽 으로 90도 꺾음
        d=(d-1)%4
    else:
        d=(d+1)%4 #D는 오른쪽으로 90도 꺾음

while 1:
    cnt+=1
    #뱀의 이동
    y+=dy[d]
    x+=dx[d]

    #범위 벗어나는경우
    if y<0 or y>=n or x<0 or x>=n:
        break
    #사과인경우
    if arr[y][x] ==2:
        #해당위치 이동
        arr[y][x] =1
        #그 자리를 q에 삽입
        q.append((y,x))
        #뱀의 움직이는 시간인 경우
    if cnt in t:
        turn(t[cnt])

    #사과가 아닌경우
    elif arr[y][x] ==0:
        #해당위치 이동
        arr[y][x] =1
        q.append((y,x))
        #이전자리 삭제해주기=> 꼬리위치 비우기 => 뱀이 이동함
        ny,nx = q.popleft()
        arr[ny][nx] = 0
        if cnt in t:
            turn(t[cnt])

    else:
        break

    for a in arr:
        for b in a:
            print(b, end=" ")
        print()
    print()

print(cnt)