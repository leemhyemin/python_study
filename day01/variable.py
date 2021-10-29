#result 변수 , = 대입,할당,저장 

n1 = 10
result = n1 + 20

print(result * 3)
result = result + 3

print(result) #33
# 선언되지 않은 변수는 사용불가!
# result = number + 10
# print(number)
print("number") # 따옴표안에 있으면 전부 텍스트로 취급(변수x)

fruit = '포도'

print(fruit + '맛있어요~')

print('=====================')

# 변수 이름 규칙
# 1. 숫자로 시작하면 안됨.
# 7number = 700
number7 = 700
num7ber = 777

# 2. 공백을 포함할 수 없음
# user birth day = 1994010
userbirthday = 19940101

user_birth_day = 19940101 # snake case (파이썬선호)
userBirthDay = 19940101 # camel case (자바,자바스크립트 선호 낙타.)

#3. 대/소문자를 구분함
banana = '바나나'
BANANA = '뻐네이너'
print (banana)
print (BANANA)

# 4. if, whtle 과 같은 이미 기능이 포함된 단어는 변수이름 사용x
# if = 123
# for = "메롱"
# whilE = 123 대/소문자구분

# 한글, 한자 변수 가능? - 가능하지만 안쓰는걸 권장
야옹이 = '고양이'
print(야옹이)
# 충돌 일으킬수 있음 영어로.
