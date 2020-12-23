# TIL 09.08_ R (팩터, 데이터프레임)

> 벡터와 팩터의 차이를 알고, 데이터프레임 생성 방법과 구조 확인하기

## 1. Factor(팩터)

> 1차원 벡터. 벡터의 값을 범주값으로 인식한다.

### (1) 팩터 생성방법

- `factor(벡터)`

```R
> score <- c(1,3,2,4,2,1,3,5,1,3,3,3)
> f_score <- factor(score) #미리 만들어진 벡터를 팩터로 변환
> class(f_score)
[1] "factor"
> f_score 
 [1] 1 3 2 4 2 1 3 5 1 3 3 3
Levels: 1 2 3 4 5 #levels : 값들의 범주 구성을 알려줌.
> summary(f_score) #갯수를 세줌. 범주형 데이터로 간주함.
1 2 3 4 5 
3 2 5 1 1 
> levels(f_score)
[1] "1" "2" "3" "4" "5"
```

- `factor(벡터,levels=레벨벡터)`

```r
> data1
[1] "월" "수" "토" "월" "목" "화"
> week.korabbname <- c("일", "월", "화", "수", "목", "금", "토")
> day2 <- factor(data1, levels=week.korabbname)
> day2
[1] 월 수 토 월 목 화
Levels: 일 월 화 수 목 금 토
> summary(day2)
일 월 화 수 목 금 토 
 0  2  1  1  1  0  1 
> levels(day2)
[1] "일" "월" "화" "수" "목" "금" "토"
```

데이터셋에 있는 데이터를 레벨에서 제외하는 경우. 해당 데이터를 NA로 처리한다.

몇가지 범주에 대해서만 레벨을 지정하고 싶을 때 사용하며, 분석 시 NA 값을 제외. 

```R
> btype <- factor( c("A", "O", "AB", "B", "O", "A"), 
+   levels=c("A", "B", "O"))
> btype
[1] A    O    <NA> B    O    A   
Levels: A B O
> summary(btype)
   A    B    O NA's 
   2    1    2    1 
> levels(btype)
[1] "A" "B" "O"
```

```R
> gender <- factor(c(1,2,1,1,1,2,1,2), 
+                  levels=c(1,2), 
+                  labels=c("남성", "여성"))
#벡터에 맞춰 각각 라벨에 지정된 명칭으로 바꿔줌
> gender
[1] 남성 여성 남성 남성 남성 여성 남성 여성
Levels: 남성 여성
> summary(gender)
남성 여성 
   5    3 
> levels(gender)
[1] "남성" "여성"
```

 

## 2. Data.Frame(데이터프레임)

> 2차원 구조. 열단위로 서로 다른 타입의 데이터들로 구성 가능하다.
>
> 단, 모든 열의 데이터 개수(행의 개수)는 동일해야 한다.

### (1) 데이터프레임 생성방법

```R
> no <- c(1,2,3,4)
> name <- c('Apple','Banana','Peach','Berry')
> qty <- c(5,2,7,9)
> price <- c(500,200,200,500)
> fruit <- data.frame(no, name, qty, price)
> fruit
  no   name qty price
1  1  Apple   5   500
2  2 Banana   2   200
3  3  Peach   7   200
4  4  Berry   9   500
```



### (2) 데이터프레임 인덱싱

```R
> fruit[1,]
  no  name qty price
1  1 Apple   5   500

> fruit[-1,]
  no   name qty price
2  2 Banana   2   200
3  3  Peach   7   200
4  4  Berry   9   500

> fruit[,2] #데이터 프레임을 유지하지 않고, 열을 벡터로 추출함
[1] "Apple"  "Banana" "Peach"  "Berry" 

> fruit[,3]
[1] 5 2 7 9
> fruit[[3]]
[1] 5 2 7 9

> fruit[,3, drop=F]  #drop 속성은 데이터프레임 구조를 유지하게 해줌
  qty
1   5
2   2
3   7
4   9
> fruit[3]
  qty
1   5
2   2
3   7
4   9

> fruit[, c(3,4)] #모든 행에 대해 3열과 4열
  qty price
1   5   500
2   2   200
3   7   200
4   9   500

> fruit[3,2]
[1] "Peach"

> fruit$qty
[1] 5 2 7 9
```

