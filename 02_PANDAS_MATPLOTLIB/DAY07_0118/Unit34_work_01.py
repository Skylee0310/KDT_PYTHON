class Knight :
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')

#34.6. 심사문제 : 게임 캐릭터 클래스 만들기
'''
게임 캐릭터 클래스
클래스 이름 : Annie
클래스 속성 : 체력
클래스 기능 : 스킬의 피해량 출력 (체력 - 스킬 피해량( AP * 0.65 + 400 ))
'''
#
class Annie :
    def __init__(self, health, mana, ap):
        self.health = health
        self.mana = mana
        self.ap = ap
    def tibbers(self):
        damage = self.ap*0.65+400
        print(f'티버 : 피해량 {damage}')
health, mana, ap = map(float, input("체력, 마나, 주문력을 입력하세요. : ").split())
x = Annie(health=health, mana=mana, ap=ap)
x.tibbers()