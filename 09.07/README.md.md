# TIL 09.07_ R (벡터, 매트릭스)

>  R --> 데이터 처리를 목적으로 만들어진 언어라는 것을 염두에 두고 공부
>
> 반복문 쓰지 않고도 다량의 데이터를 처리할 수 있게 연산자와 제어문이 잘 되어 있음.
>
> 다양한 목적의 함수를 만들고 활용할 줄 알아야 함.



## 1. Vector(벡터)

> R에서 다루는 가장 기초적인 1차원 데이터셋.
>
> 하나의 데이터 값도 벡터로 취급되며, 동일 타입의 데이터만으로 구성된다.

 ### (1) 벡터 생성방법

#### `연산자`

```R
v1 <- 1:10
v1 = 1:10
1:10 -> v1
print(v1)
```

결과

```R
> print(v1)
[1] 1 2 3 4 5 6 7 8 9 10
```

#### `c()`

- 규칙이 없을 때 주로 사용한다.

```R
v2 <- c(10, 5, 7 ,4, 15, 1)
```

#### `seq()`

- 규칙이 있을 때 주로 사용한다.
- seq(x, y, a) : x부터 y까지 a씩 증가. a디폴트값은 1

```R
seq(1,10)
seq(1, 10, 2)
seq(0, 100, 5)
```

#### `rep()`

- repeat. 반복할 때 사용하는 방법
- 키워드 파라미터 times, each

```R
> rep(1, 100) #1을 100번 반복해라.
  [1] 1 1 1 1 1 ... 1 1 1  (100개)
> rep(1:3, 5) #1,2,3을 5번 반복해라.
 [1] 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3
> rep(1:3, times=5) # 키워드 파라미터
 [1] 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3
> rep(1:3, each=5)
 [1] 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3
```



### (2) 미리 정의된 내장 상수 벡터

- LETTERS : 대문자 알파벳
- letters : 소문자 알파벳
- month.name : 월별 영어표기
- month.abb : 월별 단순 영어표기
- pi : 3.141593

```
> LETTERS[1]; LETTERS[c(3,4,5)]; LETTERS[c(-2,-4)]
[1] "A"
[1] "C" "D" "E"
[1] "A" "C" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z"
```



### (3) 벡터 주요 함수

```R
> x <- c(10,2,7,4,15)
> x
[1] 10  2  7  4 15
> print(x)
[1] 10  2  7  4 15
> class(x)
[1] "numeric"
> range(x)
[1]  2 15
> sort(x)
[1]  2  4  7 10 15
> sort(x, decreasing = TRUE)
[1] 15 10  7  4  2
> sort(x, decreasing = T)
[1] 15 10  7  4  2
```

```R
sample(1:20, 3) #1부터 20까지 중복없이 3개를 추출
sample(1:10, 7, replace=T) #1부터 10까지 중복 가능하게 7개를 추출
```

```R
> fruit <- c("Apple", "Banana", "Strawberry")
> food <- c("Pie","Juice", "Cake")
> paste(fruit, food)
[1] "Apple Pie"       "Banana Juice"    "Strawberry Cake"
```



## 2. Matrix(행렬)

> 2차원의 벡터. 동일타입의 데이터만 저장 가능

### (1) 행렬 생성방법

- matrix(data=벡터, nrow=행의 갯수, ncol=열의 갯수)
- matrix(data=벡터, nrow=행의 갯수, ncol=열의 갯수, byrow=TRUE)

byrow가 TRUE이면 행을 먼저 채운다. 디폴트는 열 먼저 채움.

```R
> x1 <-matrix(1:8, nrow = 2)
> x1
     [,1] [,2] [,3] [,4]
[1,]    1    3    5    7
[2,]    2    4    6    8
```



### (2) `rbind`, `cbind`

- rbind (벡터) : 벡터들이 행에 적용됨
- cbind(벡터) : 벡터들이 열에 적용됨

```R
> vec1 <- c(1,2,3)
> vec2 <- c(4,5,6)
> vec3 <- c(7,8,9)
> mat1 <- rbind(vec1,vec2,vec3); mat1
     [,1] [,2] [,3]
vec1    1    2    3
vec2    4    5    6
vec3    7    8    9
> mat2 <- cbind(vec1,vec2,vec3); mat2
     vec1 vec2 vec3
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9
```

예제] 다음과 같이 구성 되는 2행 3열 매트릭스 alpha를 생성한 후에

​    ![img](file:///C:/Users/zhezh/AppData/Local/Temp/msohtmlclip1/01/clip_image001.png)

​     alpha에 ‘x’, ‘y’, ‘z’ 라는 행을 추가하여 alpha2 를 만들고 출력한다.

​    alpha에 ‘s’, ‘p’ 라는 열을 추가하여 alpha3 를 만들고 출력한다.

```R
> alpha2 <- rbind(alpha,c('x','y','z'));alpha2
     [,1] [,2] [,3]
[1,] "a"  "c"  "e" 
[2,] "b"  "d"  "f" 
[3,] "x"  "y"  "z" 
> alpha3 <- cbind(alpha,c('s','p'));alpha3
     [,1] [,2] [,3] [,4]
[1,] "a"  "c"  "e"  "s" 
[2,] "b"  "d"  "f"  "p" 
```

