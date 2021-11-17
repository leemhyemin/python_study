'''
# 지역 변수
- 지역변수란 함수 내부에서 만들어진 변수를 말합니다.
- 지역변수는 함수 내부에서만 사용할 수 있으며, 함수호출이 종료되면
    메모리에서 자동제거 됩니다.
- 함수 내부에서는 지역변수 계속 쓸수 있음
- 각 다른 함수에서 같은 변수 사용 가능 
'''
# 함수부
def info():
    word = '안녕'  # 지역변수 변수(word)
    print(word)
    for c in word:
        print(c)

def greeting():
    word = 'hello'
    print(word)
# print(word) 함수 밖에서 x

#실행부
info()  #실행
greeting() 

