
# for 변수 in 
for n in range(1,11):
    print(f'{n}번 회원님 안녕하세요!')

print('='*40)
# 0,1,2 3번 
for a in range(3):
    print('메롱')

# 1~10까지의 총합
total = 0
for n in range(1,11):
    total += n 
print('1~10까지의 총합: {}'.format(total))


# 7~100까지의 정수중 7의 배수들만 가로로 출력하기
for num in range(7, 101, 7):
    print(num, end= " ") 
    
    
print('='*40)

# 1~100 까지의 정수 중 4의 배수를 가로로 출력
for num in range(1,100):
    if num % 4 == 0:
        print(num, end=" ")

print('='*40)

#1~100 까지의 정수 중 6의 배수이면서 12의 배수가 아닌 수를 가로로 출력
# 6 18 30 42
for num in range(1,101):
    if num % 6 == 0:
        print(num, end=" ")
    num += 12




# 1~9876사이의 정수중 13의 배수의 개수를 출력
# 범위 안의 13의 배수의 숫자: xxx개

num = 1
count = 0 #13 배수 숫자를 쓸 변수
for num in range(1,9877):
    if num % 13 == 0:
        count += 1
print(f'범위 안의 13의 배수의 숫자: {count}개')





