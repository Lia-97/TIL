# 딕셔너리
cabinet = {3:'유재석', 100:'김태호'}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet[5]) #프로그램이 종료됨
print(cabinet.get(5)) # None을 반환함
print(cabinet.get(5), "사용 가능") # 5번 값이 없으면 "사용 가능"을 반환함

print(3 in cabinet) #True
print(5 in cabinet) #False

del cabinet[3] #3번 값이 사라짐

#key 들만 출력
print(cabinet.keys())

#value 들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items()) #dict_items([(3,'유재석'),(100,'김태호')])

# 셋
java = {'유재석','김태호','양세형'}
python = set(['유재석','박명수'])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 줄 알지만 python 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊어버림
java.remove("김태호")
print(java)

# 자료구조의 변경
menu = ('커피','우유','주스')
print(menu, type(menu))

menu = list(menu) # tuple(menu), set(menu) 등
print(menu, type(menu))

"""
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3: random 모듈의 shuffle 과 sample 을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))
"""

# 답안
from random import *
lst = [_ for _ in range(1,21)]
shuffle(lst)
print("-- 당첨자 발표 --")
print("치킨 당첨자 :", sample(lst,1))
shuffle(lst)
print('커피 당첨자 :',sample(lst,3))
print('-- 축하합니다 --')

# 해설
from random import *
users = range(1,21) # 1부터 20까지 숫자를 생성
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print('커피 당첨자 : {0}'.format(winners[1:]))
print('-- 축하합니다 --')