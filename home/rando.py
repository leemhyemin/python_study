import random
AID={0:3,1:2,2:1,3:2} #AI가 결정할 힌트
sw=True #사람이 할 차례
sp=1
count=31
print('BR31 게임을 시작 합니다.')
print('31을 말하는 쪽이 패배 합니다.')
while count>0:
    if sw:
        print('당신의 차례 입니다.')
        n=0
        while n<1 or n>3: #1~3 사이가 아니면 계속 입력
            n=int(input('몇개 만큼말 할까요(1~3): '))
        for i in range(n):
            print(sp)
            sp+=1
            count-=1
            if sp>31:
                break
        if sp>31:
            break
        sw=False
    else:
        print('AI가 생각중 입니다. 잠시만 기다려 주세요.')
        na=count%4
        if na==1:
            n=random.randint(1,3)
        else:
            n=AID[na]
        print()
        print()
        print('AI가 말할 숫자의 갯수 :',n)
        for i in range(n):
            print(sp)
            sp+=1
            count-=1
            if sp>31:
                break
        if sp>31:
            break
        sw=True

if sw:
    print('당신의 패배 입니다')
else:
    print('와! 대단해요. AI를 이겼습니다.')
    