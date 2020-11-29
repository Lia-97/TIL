# # 숫자 처리 함수
# print(abs(-5)) # 절댓값
# print(pow(4,2)) # 4^2 =4*4
#
# from math import *
# print(floor(4.99)) #내림
# print(ceil(3.14))
# print(sqrt(16)) #제곱근
#
# # 랜덤 함수
# from random import *
# print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
# print(random()*10) # 0.0 이상 10.0 미만의 임의의 값 생성
# print(int(random()*10)) # 0 이상 10 미만의 임의의 정수값 생성
# print(int(random()*10) + 1) # 1 이상 10 이하의 임의의 정수값 생성
#
# print(randrange(1,45)) # 1이상 45 미만의 임의의 값 생성
# print(randint(1,45)) # 1이상 45이하의 임의의 값 생성

"""Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1: 랜덤으로 날짜를 뽑아야 함.
조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3: 매월 1~3일은 스터디 준비를 해야 하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다."""

# from random import *
# date = randint(4,28)
# print('오프라인 스터디 모임 날짜는 매월',date,'일로 선정되었습니다.')
# print('오프라인 스터디 모임 날짜는 매월 '+str(date)+' 일로 선정되었습니다.')

# # 문자열처리함수
# python = 'Python is Amazing'
# print(python[0].isupper())  #True (첫번째 문자가 대문자인가?)
# print(python.replace('Python','Java'))  # 'Java is Amazing'

# # 문자열포맷
#
# # 방법1
# print('나는 %d살입니다.' % 20) # d는 정수를 의미
# print('나는 %s을 좋아해요.' % '파이썬') # s는 문자열(정수도 가능) 의미
# print('Apple 은 %c로 시작해요.' % 'A') # c는 한글자를 의미(character)
# print('나는 %s색과 %s색을 좋아해요.' %('파란','빨간'))
#
# # 방법2
# print('나는 {}살입니다.'.format(20))
# print('나는 {}색과 {}색을 좋아해요.'.format('파란','빨간'))
# print('나는 {1}색과 {0}색을 좋아해요.'.format('파란','빨간'))

# # 방법3
# print('나는 {age}살이며, {color}색을 좋아해요.'.format(age = 20, color = '빨간'))
#
# # 방법4
# age = 20
# color = '빨간'
# print(f'나는 {age}살이며, {color}색을 좋아해요.')

# # 탈출문자
#
# # \n : 줄바꿈
# print('백문이 불여일견\n백견이 불여일타')
# # \" \' : 문장 내에서 따옴표
# print("저는 \"이지혜\"입니다.")
# # \\ : 문장 내에서 \
# print('\\')
# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine") #?????????
# # \b : 백스페이스 (한글자 삭제)
# print("Redd\bApple")
# # \t : 탭
# print("Red\tApple") #?????????

"""Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1: http://부분은 제외 => naver.com
규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 +"!"로 구성

예) 생성된 비밀번호 : nav51!
"""

# #내 답안
# ad = "http://naver.com"
# dot = ad.find('.')
# word = ad[7:dot]
# key1 = word[:3]
# key2 = len(word)
# key3 = word.count('e')
# print(key1,key2,key3,'!',sep="")
#
# #해설
# url = "http://naver.com"
# my_str = url.replace('http://','')
# my_str = my_str[:my_str.index('.')]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
# print("{0}의 비밀번호는 {1}입니다.".format(url,password))