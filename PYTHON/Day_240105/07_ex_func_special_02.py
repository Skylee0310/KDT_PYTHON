#다양한 함수의 형태 -  특별한 함수 (2)
#-매개변수의 개수를 유동적으로 가변으로 하는 함수
#-키와 값의 덩어리 데이터
# 형태 : def 함수명 (**data) :
# 가변 인자 함수
# 매개변수 개수 : 0개 ~ N개
# 호출 : 함수명(키1=값1)
#       함수명(키1=값1,키2=값2,키3=값3)
#       함수명()
#------------------------------------------------------------------------------
if False :
    aDict = {'name':'Hong', 'age':10}
    aDict.update(job='학생')
    aDict.update(job='학생', birth='1112', blood='A')
    print(aDict)
#------------------------------------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinMember
# 매개 변수 : 이름, 전화 번호, 아이디, 이메일, 취미, 주소, 생일
#           가변 인수 + 전달 데이터 정보
#           키워드 파라미터 **member
# 반환값 : '가입 완료 되었습니다.'
#------------------------------------------------------------------------------
def joinMember(**member) : #key=value 값을 받는다.
    #print(type(member))
    # 멤버 저장소에 멤버 추가하기
    #mList.append(member) #-> 리스트
    #members.update(**member) #-> 딕셔너리
    members[f'M {len(members)}']=member
    print(member)
    # members[len(member)+1] = member
    # for k, v in member.items() :
    #     print(k,v)
#-----------------------------------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinMember2
# 매개 변수 : 필수 => id, pw
#           선택 => **option 이름, 전화 번호, 이메일, 취미, 주소, 생일...
#           가변 + 데이터 정보 함께
# 반환값 : '가입 완료 되었습니다.
#------------------------------------------------------------------------------
def joinMember2(id, pw, **option) : #id, pw는 없으면 실행 불가능.
    print('ok')
#------------------------------------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinMember3
# 매개 변수 : 필수 => id, pw, loc, gender
#           선택 => **option 이름, 전화 번호, 이메일, 취미, 주소, 생일...
#           가변 + 데이터 정보 함께
# 반환값 : '가입 완료 되었습니다.
def joinMember3(id, pw, loc='내국인', gender='남자', **option) : #loc, gender 입력 안하면 기본값.
    print(id, pw, loc, gender, option)
# 키 => id
# 값 => pw, loc='내국인', gender='남자', **option
#       {'pw':'123', 'loc':'내국인', 'gender'='남자', 'ect':'{option}}
    valueDict = {}
    valueDict['pw'] = pw
    valueDict['loc'] = loc
    valueDict['gender'] = gender
    valueDict['etc'] = option
    members[id] = valueDict
    print(f'[AF] : {members}')
    # for m in members.items() :
    #     print(m)


# 함수 사용, 호출
#------------------------------------------------------------------------------
#가입된 회원들 저장 변수
members= {}
mList = []


#회원가입 기능 함수 호출
print(f'[BF] : {members}')
joinMember3('h', 'ph', gender='여자', name='hong', age=17, birth='2020')
joinMember2('Hong84', 'ph', phone='010', job='doctor', blood = 'b')
# joinMember(id='baby', birth='2024', blood='A')

print(f'[AF] : {members}')
# m = {'name':'hong', 'age':17}
# print(m.keys())
# print(m.values())
# print(m.items())
#--------------------------------------------------------------------------------------------------------------------
