# STACK

- 입력과 출력이 한 곳(방향)으로 제한

- LIFO (Last In First Out, 후입선출) : 가장 나중에 들어온 것이 가장 먼저 나옴

  

![image-20221226204038783](C:\Users\dhkdw\AppData\Roaming\Typora\typora-user-images\image-20221226204038783.png)



*** 변수**

1. 스택 포인터(ptr)

 : 현재 스택에 데이터가 어디까지 쌓여있는지 나타내는 포인터. 

2. 크기(capacity)

 : 스택의 크기를 나타내는 변수. 스택 생성 시 지정해준다.

 

*** 함수**

1. __init__() : 변수 초기화

2. push() : 스택에 데이터를 한개 삽입한다.

3. pop() : 스택에서 데이터를 한개 꺼낸다.

4. __len__() : 현재 쌓여있는 데이터의 크기를 반환한다.

5. is_empty() : 스택의 empty 여부를 확인한다.

6. is_full() : 스택이 가득 찼는지 확인한다.

7. peek() : 가장 최근에 쌓인 데이터를 읽는다.



- push와 pop을 할 때, 해당 인덱스 위치를 알아야 하므로 '스택 포인터 SP'가 팔요함

- 1. 스택 포인터는 항상 빈 공간을 가리키고 있다.

  2. 포인터의 위치만을 수정하여 스택초기화, 데이터 제거가 가능하다.





## 구현

```python
from typing import Any

class Stack:



    class Empty(Exception):
        pass

    class Full(Exception):
        pass
    

    def __init__(self, c:int) -> None:
        ## 변수 초기화 함수.
        ## stack의 크기를 생성 시 전달받는다.
        self.ptr = 0
        self.capacity = c
        self.stk = [None] * c

    def __len__(self) -> int:
        ## Stack의 길이를 반환하는 함수
        ## ptr은 다음 빈 공간을 가리키고 있기 때문에 길이와 같다.
        return self.ptr

    def is_empty(self) -> bool:
        ## Stack이 비었는지 확인하는 함수
        return self.ptr <= 0

    def is_full(self) -> bool:
        ## Stack이 가득 찼는지 확인하는 함수
        return self.ptr >= self.capacity

    def push(self, data: int) -> None:
        if self.is_full():
            raise Stack.Full
        self.stk[self.ptr] = data
        self.ptr += 1

    def pop(self) -> any:
        ## Stack의 가장 바깥에 쌓여있는 데이터를 Stack에서 빼는 함수.
        ## 비었는지 확인하고 data를 return한다. 이 때 ptr만 하나 줄여주면 된다.
        if self.is_empty():
            raise Stack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self):
        ## 가장 바깥에 쌓여있는 데이터를 읽어오는 함수
        ## 비어있는지 확인 후 data를 return한다.
        if self.is_empty():
            raise Stack.Empty
        return self.stk[self.ptr-1]
```





# Queue

- 입력과 출력을 한 쪽 끝(front, rear)로 제한
- FIFO (First In First Out, 선입선출) : 가장 먼저 들어온 것이 가장 먼저 나

- 큐의 가장 첫번째 원소를 front, 마지막 원소를 rear라 함

- 큐는 들어올 때 rear로 들어오고, 나갈 때는 front부터 나감

  

![image-20221226210835970](C:\Users\dhkdw\AppData\Roaming\Typora\typora-user-images\image-20221226210835970.png)



*** 함수**

1. __init__() : 변수 초기화

2. enqueue() : 큐에 데이터를 한개 삽입한다.

3. dequeue() : 큐에서 데이터를 한개 꺼낸다.





## 구현



```python

 
#클래스 선언
class Queue:
 
    # 초기 설정, 스택으로 사용할 리스트 선언
    def __init__(self):
        self.queue = []
 
    # In 함수 / insert 함수 List의 Insert 함수 이용
    def enqueue(self, data):
        self.queue.insert(0, data)
 
    # Out 함수 / Remove 함수, List의 pop함수 이용
    def dequeue(self):
        if len(self.queue) <=0 :
            return("빈 큐입니다.")
        else :
            return self.queue.pop()
 
        
```

