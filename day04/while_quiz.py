# 정수 2개 입력가능한 프로그램
# 5+6+7+8 26 

num1 = int(input("정수1: "))
num2 = int(input("정수2: "))

total = 0
while num1 <= num2:
    total += num1
    num1 += 1

print(f'총합: {total}')

