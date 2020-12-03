# # 표준입출력
#
# scores = {'수학':80, '국어':60, '코딩': 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=':') # 8(4)칸의 공간을 확보한 상태에서 왼쪽(오른쪽) 정렬
#
# # 은행 대기순번표 (001, 002, 003, ...)
# for num in range(1, 21):
#     print('대기번호 : ' + str(num).zfill(3)) # 3칸의 공간을 확보하고, 값이 없는 빈 공간은 0으로 채운다
#
# answer = input('아무 값이나 입력하세요 : ') # input으로 받은 값은 str이다.
# print(type(answer))
# print('입력하신 값은 '+answer+'입니다.')
#
# #  다양한 출력포맷
#
# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print('{0: >10}'.format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print('{0: >+10}'.format(500))
# # 왼쪽 정렬하고, 빈칸을 _로 채움
# print('{0:_<+10}'.format(500))
# # 세자리 마다 콤마를 찍어주기
# print('{0:,}'.format(50000000000))
# # 세자리 마다 콤마를 찍어주기, +- 부호 붙이기
# print('{0:+,}'.format(50000000000))
# # 세자리 마다 콤마를 찍어주기, +- 부호 붙이기, 자릿수 확보하기, 빈자리는 ^로 채우기
# print('{0:^<+30,}'.format(20000000000000))
# # 소수점 출력
# print('{0:f}'.format(5/3))
# # 소수점 특정 자리수 까지만 표시
# print('{0:.2f}'.format(5/3)) #소수점 셋째자리에서 반올림
#
# #파일 입출력
# score_file = open('score.txt','w',encoding='utf8') # score.txt 파일을 쓰기 용도로 연다
# print('안녕? 나는 지혜', file=score_file) # score_file에 내용을 적는다
# print('너는 이름이 뭐니?', file=score_file)
# score_file.close() # score_file을 닫는다

# score_file = open('score.txt','a',encoding='utf8') # 덮어쓰기
# score_file.write('내 이름은 지원')
# score_file.write('\n만나서 반가워')
# score_file.close()

# # 파일 읽어오기
# score_file = open('score.txt','r',encoding='utf8')
# print(score_file.read())
# score_file.close()

# score_file = open('score.txt','r',encoding='utf8')
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# score_file.close()

# score_file = open('score.txt','r',encoding='utf8')
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# score_file = open('score.txt','r',encoding='utf8')
# lines = score_file.readlines() #모든 line을 읽어서 list 형태로 저장
# for line in lines:
#     print(line,end='')
#
# score_file.close()

# # 피클
#
# import pickle
# profile_file = open('profile.pickle','wb')
# profile = {'이름':'이지혜','나이':25, '취미':['수영','요가']}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file에 저장
# profile_file.close()
#
# profile_file = open('profile.pickle','rb')
# profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()

# import pickle
# with open('profile.pickle', 'rb') as profile_file:
#     print(pickle.load(profile_file))

# with open('study.txt','w',encoding='utf8') as study_file:
#     study_file.write('파이썬 공부중이에요')
#
# with open('study.txt','r',encoding='utf8') as study_file:
#     print(study_file.read())

"""
Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- x 주차 주간보고 -
부서 :
이름 :
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.
"""

for i in range(1,51):
    with open(str(i)+'주차.txt','w',encoding='utf8') as report_file:
        report_file.write('- {0} 주차 주간보고 -'.format(i))
        report_file.write('\n부서 :')
        report_file.write('\n이름 :')
        report_file.write('\n업무 요약 :')