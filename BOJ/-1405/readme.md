# 미친 로봇 스페셜 저지

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| :-------- | :---------- | :--- | :--- | :-------- | :-------- |
| 1 초      | 128 MB      | 8858 | 3529 | 2464      | 36.531%   |

## 문제

통제 할 수 없는 미친 로봇이 평면위에 있다. 그리고 이 로봇은 N번의 행동을 취할 것이다.

각 행동에서 로봇은 4개의 방향 중에 하나를 임의로 선택한다. 그리고 그 방향으로 한 칸 이동한다.

로봇이 같은 곳을 한 번보다 많이 이동하지 않을 때, 로봇의 이동 경로가 단순하다고 한다. (로봇이 시작하는 위치가 처음 방문한 곳이다.) 로봇의 이동 경로가 단순할 확률을 구하는 프로그램을 작성하시오. 예를 들어, EENE와 ENW는 단순하지만, ENWS와 WWWWSNE는 단순하지 않다. (E는 동, W는 서, N은 북, S는 남)

## 입력

첫째 줄에 N, 동쪽으로 이동할 확률, 서쪽으로 이동할 확률, 남쪽으로 이동할 확률, 북쪽으로 이동할 확률이 주어진다. N은 14보다 작거나 같은 자연수이고, 모든 확률은 100보다 작거나 같은 자연수 또는 0이다. 그리고, 동서남북으로 이동할 확률을 모두 더하면 100이다.

확률의 단위는 %이다.

## 출력

첫째 줄에 로봇의 이동 경로가 단순할 확률을 출력한다. 절대/상대 오차는 10-9 까지 허용한다.

## 예제 입력 1 복사

```
2 25 25 25 25
```

## 예제 출력 1 복사

```
0.75
```

## 예제 입력 2 복사

```
1 25 25 25 25
```

## 예제 출력 2 복사

```
1.0
```

## 예제 입력 3 복사

```
7 50 0 0 50
```

## 예제 출력 3 복사

```
1.0
```

## 예제 입력 4 복사

```
14 50 50 0 0
```

## 예제 출력 4 복사

```
0.0001220703125
```

## 예제 입력 5 복사

```
14 25 25 25 25
```

## 예제 출력 5 복사

```
0.008845493197441101
```