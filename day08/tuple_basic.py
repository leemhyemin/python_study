# 값이 고정되는 리스트 튜플.

scores = (87, 92, 23, 45, 100)
print(type(scores))

print(scores)
print(scores[1])
print(scores[1:4]) #123

total = 0 
for s in scores:
    total += s
print(f'총점: {total}점, 평균: {total / len(scores)}저ㅕㅁ')

print('='*40)
tu = 1, 3, 5, 7, 9 #튜플 만들때 ()생략 가능.
# 튜플로 가능한 문법(내부 원본 데이터를 바꾸지 않는 행위)
# 복사
print(tu[3])
print(tu[1:3])
print(tu)

print(tu + (10, 11))
print(tu)
# 튜플로 불가능한 문법( 원본 내부 데이터가 변경되는 행위)
# tu[2] = 20 #ex)
# tu.append(10)
# del(tu[1
# 
# 
# 튜플이 지원하는 함수는 index(), count()입니다.
# 튜플과 리스트는 언제든지 상호변경이 가능합니다.
print('='*40)

P = [1,2,3,4,5,6]
# 변환 할때는 튜플함수
P = tuple(p)
print(type(p))
# p[1] = 100

p = list(p)

p[1] = 100
print(p)