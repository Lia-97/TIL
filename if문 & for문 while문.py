# continue 와 break 의 차이 알기
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# 한줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 --> 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ['Iron man','Thor','I am groot']
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ['Iron man','Thor','I am groot']
students = [i.upper() for i in students]
print(students)

"""
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
"""

from random import *

sum = 0
for i in range(1, 51):
    time = randint(5, 51)
    if 5 <= time <= 15:
        sum += 1
        print('[O] ' + str(i) + '번째 손님 (소요시간 : ' + str(time) + '분)')
    else:
        print('[ ] ' + str(i) + '번째 손님 (소요시간 : ' + str(time) + '분)')
print('총 탑승 승객 :', sum, '분')

# 포맷팅 방식으로 풀어보기
from random import *

sum = 0
for i in range(1, 51):
    time = randint(5, 51)
    if 5 <= time <= 15:
        sum += 1
        print('[O] {0}번째 손님 (소요시간 : {1}분)'.format(i,time))
    else:
        print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(i,time))
print('총 탑승 승객 :', sum, '분')