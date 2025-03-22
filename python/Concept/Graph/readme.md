# 그래프

## 개요

- 그래프는 아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계를 표현한다
- 그래프는 정점(Vertex)들의 집합과 이들을 연결하는 간선(Edge)들의 집합으로 구성된 구조
  - 구조
    - ㅣvㅣ: 정점의 갯수 , ㅣEㅣ: rmfovmdp vhgkaehls rkstjsdml rotn
    - ㅣvㅣ개의 정점을 가지는 그래프는 최대 (ㅣvㅣ-1)/2 간선이 가능
      - ex) 5개의 정점이 있는 그래프의 최대 간선 수는 5*4/2개이다.

## 간선의 표현

- 간선의 정보를 저장하는 방식, 메모리나 성능을 고려해서 결정

### 인접행렬

- ㅣvㅣ* ㅣvㅣ 크기의 2차원 배열을 이용해서 간선 정보를 저장
- 배열의 배열(포인터 배열)

- 인접리스트
  - 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
- 간선의 배열
  - 간선(시작 정점, 끝 정점)을 배열에 연속적으로 저장

```python
#v 마지막정점 번호, e 간선수
v,e = map(int,input().splite())
arr= list(map(int,input().splite()))
adjm=[[0]* (v+1) for _ in range(v+1)]
for i in range(e):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjm[n1][n2]=1

```

### 연결리스트

```python
#v 마지막정점 번호, e 간선수
v,e = map(int,input().splite())
arr= list(map(int,input().splite()))
adjm=[[] for _ in range(v+1)]
for i in range(e):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjm[n1].append(n2)
    adjm[n2].append(n1) #무향그래프인 경우

```



## 그래프 순회(탐색)

- 그래프 순회는 비선형구조인 그래프로 표현된 모든 자료(정점)를 빠짐없이 탐색하는 것을 의미히ㅏㄴ다.
- 두가지방법
  - 깊이 우선 탐색 DFS
  - 너비 우선 탐색 BFS

### DFS

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마자막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 스택구조 사용

- 스택의 특성
  - 선형구조
  - 마지막에 삽입한 자료 꺼냄

```python
#dfs 재귀
def DFS(G,v):
	visited[v] =True #방문설정
    for a in graph[v]:
        if visited[a] =! True:
            DFS(G,a)
```

```python
#dfs 반복
stack = []
visited=[]
def DFS(G,v):
    stack.append(v)
    while stack:
        v = stack.pop(0)
        if not visited in v:
            visited.append(v)
            for i in graph[v]:
                if i not in visited:
                    stack.append(i)
```

```python
#코드
#v 마지막정점 번호, e 간선수
v,e = map(int,input().splite())

visited=[0]* (v+1)
def DFS(i):
    visited[i] =1
    for j in range(v+1): #i에 인접한 모든 노드에 대해
        if adjm[i][j] and visited[j]==0: #아직 방문하지 않은 곳이면
            DFS(j)
    
```

### BFS

- 너비우선탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에ㅡ, 방문했던 정점을 시작으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자료구조 QUE를 활용함

```python
def BFS(G,v) //G 그래프 v 탐색 시작점
	큐 생성
	시작점 v를 큐에 삽입
	점 v를 방문한 것으로 표시
	while 큐가 비어있지 않은 경우
		t = 큐의 첫번째 원소 반환
		for t와 연결된 모든 선에 대해
			u = t의 이웃점
			u가 방문되지 않은 곳이면,
			u를 큐에 넣고, 방문한 것으로 표시
```





## 최소 신장트리 mst

- 그래프에서 최소 비용 문제
  - 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
  - 두 정점 사이의 최소 비용의 경로 찾기
- 신장 찾기
  - n개의 정점으로 이루어진 무방향 그래프에서 정점 n-1 개의 간선으로 이루어진 트리
- 최소신장트리
  - 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소 신장트리

### Prim 알고리즘

- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식

  1.임의 정점을 하나 선택해서 시작

  2.선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택

  3.모든 정점이 선택될 때 까지 1,2과정을 반복

- 서로소인 2개의 집합 정보를 유지
  - 트리정점들 -MST를 만들기 위해 선택된 정점들
  - 비트리 정점들 - 선택되지 않은 정점들

```python
#알고리즘
def MST_PRIM(G,r): #G 그래프 r 시작 정점
	for u in G,V:
        u.key = 무한대 #u.key = u에 연결된 간선중 최소 가중치
        u.pi = null  # u.pi = 트리에서 u의 부모
    r.key = 0
    Q = G,V # 우선순위 Q에 모든 정점 넣는다.
    while Q: #Q가 있는 경우 반복
        u = Extract_MIN(Q) #key 값이 가장 작은 정점 가져오기
        for v in G.adj[u]: #u의 인접 정점들
        	if v in Q and w(u,v) < v.key: #Q에 있는 V의 key값 갱신
                v.pi = u
                v.key = w(u,v)
```

```python
def PRIM(r,v):
	MST = [0] *(v+1)
    MST[r] =1 
    s=0 #최소 가중치의 합
    for _ in ranve(v):
        u=0
        minv=1000000
        for i in range(v+1): #MST에 포함된 정점i와 인접한 정점j 중 MST
            if MST[i]==1:
                for j in range(v+1):
                    if 0<adjm[i][j]<minv and MST[j]==0:
                        u=j
                        minv = adjm[i][j]
   		s+=minv
        MST[u] =1
   return s
```



### KRUSKAL 알고리즘

- 간선을 하나씩 선택해서 MST를 찾는 알고리즘

  1. 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬

  2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴

     -사이클이 존재하면 다음으로 가중치가 낮은 간선 선택

  3. N-1개의 간선이 선택될 때 까지 2를 반복

## 최단경로

- 최단경로 정의
  - 간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로
- 하나의 시작 정점에서 끝 정점까지의 최단경로
  - 다익스트라 알고리즘
    - 음의 가중치를 허용하지 않음
  - 벨만-포드 알고리즘
    - 음의 가중치 허용
- 모든 정점들에 대한 최단경로
  - 플로이드- 워샬 알고리즘

### 다익스트라 알고리즘

- 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식이다.
- 시작정점(s)에서 끝정점(t) 까지의 최단 경로에 정점 x가 존재한다.
- 이때, 최단경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단경로로 구성된다.
- 탐욕 기법을 사용한 알고리즘으로 MST 의 프림 알고리즘과 유사하다

```python
'''
s:시작 정점, A:인접행렬, D:거리
V:정점 집합, U:선택된 정점 집합
'''
def Dijkstra(s,A,D):
    U = {s};
    for 모든 정점 v
    	D[v] = A[s][v]
    while u=! v
    	D[w]가 최소인 정점 w in V-U를 선택
        U = U and {w}
        
        for w에 인접한 모든 정점 v
        	D[v] = min(D[v], D[w]+A[w][v])
```

```python
def dijkstra(s,v):
    U = [0]*(V+1) #비용이 결정된 정점 표시
    U[s] =1	#출발점 비용 결정
    for i in range(v+1):
        D[i] = adjm[s][i]
    #남은 정점의 비용 결정
    for _ in range(V): #남은 정점 개수만큼 반복
        # D[w]가 최소인 w 결정, 비용이 결정되지 않은 정점 w 중에서
        minv = INF
        w= 0
        for i in range(V+1):
            if U[i]==0 and minV > D[i]:
                minv =D[i]
                w = i
        U[w] = 1 #비용 결정
        for v in range(V+1):
            if 0<adjm[w][v] < INF:
                D[v]  =  min(D[v], D[w]+adjm[w][v])
INF = 1000000
#v 마지막정점 번호, e 간선수
v,e = map(int,input().splite())
adjm=[[INF]* (v+1) for _ in range(v+1)]
for i in range(v+1):
    adjm[i][i]=0
for _ in range(e)
```

