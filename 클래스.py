# # 클래스
#
# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = '마린' # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력
#
# print('{} 유닛이 생성되었습니다.'.format(name))
# print('체력 {0}, 공격력 {1}\n'.format(hp, damage))
#
# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드/시즈 모드
# tank_name = '탱크' # 유닛의 이름
# tank_hp = 150 # 유닛의 체력
# tank_damage = 35 # 유닛의 공격력
#
# print('{} 유닛이 생성되었습니다.'.format(tank_name))
# print('체력 {0}, 공격력 {1}\n'.format(tank_hp, tank_damage))
#
# def attack(name, location, damage):
#     print('{0} : {1} 방향으로 적군을 공ㄱㄱ 합니다. [공격력 {2}]'.format(name,location,damage))
#
# attack(name, '1시', damage)
# attack(tank_name, '1시', tank_damage)
#
# # 새로운 유닛이 생겼을 때마다 변수를 만들수는 없음 --> 클래스가 필요한 이유

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성 되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

marine1 = Unit('마린',40,5)
marine2 = Unit('마린',40,5)
tank = Unit('탱크',150,35)

# 멤버변수 --> 클래스 내에서 정의된 변수