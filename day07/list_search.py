

scores = [99, 14, 87, 100, 55, 100, 99, 100]
# count를 넣으면 그 데이터가 몇개인지 세줌.
print(f'만점자의 수는 {scores.count(100)}명입니다.')
print(f'87이 저장된 인덱스: {scores.index(87)}') #저장된 리스트 번호
print(f'학생 수는 {len(scores)}명 입니다.') # len 길이를 세줍니다
print(f'최고 점수는 {max(scores)}점입니다.') #최대
print(f'최고 점수는 {min(scores)}점입니다.') #최소

print('='*40)

foods = ['김밥', '단무지', '닭강정', '라면'] #리스트

print('단무지'in foods)
print('짜장면'in foods)
print('김밥' not in foods)

f = input('음식명: ')

# 리스트 내의 데이터 저장 유무를 판단할 때는 in을 사용
if f in foods:
    print('해당 메뉴는 존재하는 메뉴입니다.')
else:
    print('없는 메뉴입니다.')

