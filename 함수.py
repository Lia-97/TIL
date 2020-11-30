# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

# 전달값과 반환값
def deposit(balance, money):
    print('입금이 완료되었습니다. 잔액은 {0} 원입니다.'.format(balance + money))
    return balance +money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었씁니다. 잔액은 {0} 원입니다.".format(balance + money))
        return balance - money
    else:
        print('출금이 불가능합니다. 잔액은 {0}')