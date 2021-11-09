# 수정전:['영웅재중', '최강창민', '유노윤호', '시아준수', '믹키유천']
# 수정할 이름을 입력:
# 그런멤버는 없어
# 수정완료
# 새로운이름: 
name = ['영웅재중', '최강창민', '유노윤호', '시아준수', '믹키유천']

while True:
    print("\n수정전:" , name)
    n = input('수정할이름을 입력: ')
    if n in name:
        new_name = input('새로운이름: ')
        name[name.index(n)] = new_name
        print('수정완료!')
        print('\n수정후:', name)
        break
    else:
        print('그런 멤버는 없어~~')


    
