#  [] = 리스트  () = 튜플  {} = 딕셔너리 *사물함 느낌*  {'허준'}= 셋 *보따리*
# 집합(set)
# ^순서^가 없이 빠르게 저장, 중복저장 허용 x 
names = {'허준', '신사임당', '권율', '홍길동', '허준'}
#  허준 중복
print(type(names))
print(len(names))
print(names)
# for 문은 in뒤에 쓸수 있는 타입 리스트,튜플,딕셔너리,셋,문자열(str)
# 숫자 x 변수 x true논리 x
for x in names:
    print(x)

# 빈 집합 만들기 set()
s = set()
print(type(s))
print(s)

# set에 데이터 추가 / 삭제
asia = {'한국','중국','일본'}
print(asia)
# set 추가 .add
asia.add('태국')
asia.add('중국') # 중복은 x
print(asia)

# .remove('지우고싶은 이름')
asia.remove('일본')
print(asia)

# 결합(합집합) update함수
asia2 = {'이라크', '싱가포르', '한국'}
asia.update(asia2)
print(asia)




