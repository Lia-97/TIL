# TIL(10.01)_Stack 이해하기

- 스택 : LIFO(last in first out, 선입후출)

  스택을 이해하기에 적절한 그림은 다음과 같다.

  데이터 저장소에 새로 들어오는 데이터의 위치는 저장소의 끝 부분(top)이고, 내보내는 데이터 역시 저장소의 top에서 나간다.

  

![4_ 파이썬으로 스택(Stack) 자료구조 구현하기](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99BF11415AB4C98120)   

​    	

​		push : 입력, item을 쌓아 올리는 작업

​		pop : 출력, tiem에서 제일 위의 것을 꺼내는 작업

​		peek : top의 위치에 있는 데이터를 확인하는 것.



스택 자료구조의 pop기능을 구현하는 것은 파이썬의 내장함수 pop()을 사용하는 것과 같다.

이해를 돕기 위해 스택의 pop 기능을 구현하는 코드를 서칭해보았다.

이곳에 다시 적어보며 복습해보고자 한다.

```python 
#스택 클래스 정의
class Stack(list):
    push = list.append
    
    def is_empty(self):
        if not self:
            return True
        else:
            return False
        
    def peek(self):               #최상단 데이터 확인
        return self[-1]
    
if __name__=="__main__":          #프로그램의 시작점일 때만 아래 코드 실행
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    
    while s:
        data = s.pop()
        print(Data, end ' ')       # 3 2 1
```

그렇다면 여기서 궁금증.

```python
if__name__="__main__":
```

해당 코드는 무엇을 확인하기 위한 것일까?

파이썬은 name__변수를 통해 현재 스크립트 파일이 시작점인지 모듈인지 판단한다.

위의 코드는 현재 스크립트 파일이 프로그램의 시작점이 맞는지 판단하는 작업이다.

즉 name 변수의 값이 main이라면 현재 스크립트 파일이 프로그램의 시작점이라는 것이다.