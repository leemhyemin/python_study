###########################################
# 함수 정의 
def add(n1, n2):
    print(f'{n1}, {n2}')
    return n1 + n2
    # a = 10 return 밑은 실행 x

def sub(n1, n2):
    res = n1 - n2
    return res

#  return 필요 없는 함수#####################
def multi(n1, n2):
    print(f'{n1} x {n2} = {n1 * n2}')

def infinite_loop():
    while True:
        msg = int(input('>>> '))

        if msg == 0:
            print('break!!')
            break
        elif msg ==1:
            print('continue!!')
            continue
        elif msg ==2:
            print('return!')
            return 

        print('하하호호')
    print('함수 이제 끝남')

# 사칙연산
def operate_all(n1, n2):
    # return [add(n1, n2), sub(n1, n2), n1*n2, n1/n2]
    return {
        'add': add(n1, n2)
        , 'sub': sub(n1, n2)
        , 'mul': n1 * n2
        , 'div': n1 / n2
    }
# 리스트, 딕셔너리 응용 
# 함수 안에 다른 함수를 부를수 있음

############################################
# 실행부
if __name__ == '__main__':
    
    add(10, 5)
    print(add(10, 5))

    add(100, 200)
    result = add(100, 200)
    print(result)

    resslt2 = sub(100, 20)
    print(resslt2)

    multi(3, 7)
    # x = multi(3, 7)
    # print(x) return 없는 함수는 변수 x
    
    resslt3 = add(add(add(2, 3), 8), 11) # 제일 안쪽부터 return
    print(resslt3)

    # add(multiA(3,3), sub(20,10)) return이 없는 함수를 안에 x
    multi(add(4, 7), sub(10, 4)) 

    print('='*40)

    # infinite_loop()

    result_list = operate_all(10, 5)
    print(result_list)
    print(result_list['mul'])