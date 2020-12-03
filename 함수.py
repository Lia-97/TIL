# # 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
#
# # 전달값과 반환값
# def deposit(balance, money):
#     print('입금이 완료되었습니다. 잔액은 {0} 원입니다.'.format(balance + money))
#     return balance +money
#
# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었씁니다. 잔액은 {0} 원입니다.".format(balance + money))
#         return balance - money
#     else:
#         print('출금이 불가능합니다. 잔액은 {0}원입니다.'.format(balance + money))
#         return balance
#
# def withdraw_night(balance, money):
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission
#
# balance = 0
# balance = deposit(balance, 1000)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission,balance))

# # 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
#
# profile('이지혜', 25, 'python')
# profile('이지원', 25, 'java')

# # 같은 학교 같은 학년 같은 반 같은 수업. --> 기본값 사용
# def profile(name, age=17, main_lang='python'):
#      print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
#
# profile('이지혜')
# profile('이지원')
# profile('이지수',26)

# # 키워드 값
# def profile(name, age=17, main_lang='python'):
#     print(name, age, main_lang)
#
# profile(name="이지혜",main_lang='python', age=25) # 키워드를 이용해서 함수를 호출하면, 키워드에 해당하는 값이 리턴된다.

# # 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=' ')
#     print(lang1,lang2,lang3,lang4,lang5)
#
# profile('이지혜',25,'python','java','c','c#','c++')
# profile('이지원',20,'kotlin','swift','','','') # 개수를 맞춰야하는 불편함이 존재
#
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=' ')
#     for lang in language:
#         print(lang, end=' ')
#     print()
#
# profile('이지혜',25,'python','java','c','c#','c++','javascript')
# profile('이지원',20,'kotlin','swift')

# # 지역변수, 전역변수
# gun = 10
#
# def checkpoint(soldiers): #경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print('[함수 내] 남은 총 : {0}'.format(gun))
#
# print('전체 총 : {0}'.format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
# print('남은 총 : {0}'.format(gun))

"""
Quiz) 표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
"""

def std_weight(height, gender):
    if gender == '남자':
        return height * height * 22
    elif gender == '여자':
        return height * height * 21

height = 175
gender = '남자'
weight = round(std_weight(height/100, gender),2)
print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.'.format(height, gender, weight))