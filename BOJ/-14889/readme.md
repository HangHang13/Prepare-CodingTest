# 😇BOJ 14889 스타트 링크

## 👺필요한 개념

- for문 루프문 활용
- 조합
- itertools


## 👺풀이과정

- 투포인터 활용? 앞이랑 가장 마지막 참조할 수 있도록하기

## 👺코드

```python
import itertools
#sys.stdin=open('input.txt')

#입력
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))

    #n만큼 플레이어 숫자만들기
player= [i for i in range(n)]

#print(f'player : {player}')
#player : [0, 1, 2, 3]


#n만큼 플레이어중, n//2만큼 조합으로 팀을 나눔
team=[]
for a in itertools.combinations(player, n//2):
    team.append(list(a))
#print(f'team : {team}')
#team : [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]


ans=[]
#투포인터 활용? 맨앞이랑  맨마지막 참조할 수 있도록하기 앞에 1증가시 뒤에 1감소하는 식으로
for t in range(len(team)//2):
    #초기화
    AA=0
    for y in team[t]:
        for x in team[t]:
            AA+=arr[y][x]
         
        	#0,0 1,1 2,2, 3,3 은 모두 0이므로 더해줘도 상관없음
            #위 경우 AA+= arr[0][0]+arr[0][1]+arr[1][0]+arr[1][1]
            #AA+=arr[0][1]+arr[1][0]
            
    #초기화
    BB=0
    for y in team[-(t+1)]: 
        for x in team[-(t+1)]:
            BB+=arr[y][x]
            #위 경우 BB+= arr[2][3]+arr[2][2]+arr[3][2]+arr[3][3]
            #BB+=arr[2][3]+arr[3][2]
            
    ans.append(abs(BB-AA)) #t를 실행하면서 그 최소값들을 리스트에 더해줌
    
print(min(ans)) # t반복후, 가장작은 값 도출하기

```

