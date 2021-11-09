# 삭제전:'[영웅재중', '최강창민', '유노윤호', '시아준수', '믹키유천']
# 삭제할 이름을 입력하세요!
# > name
# name는(은) 없는 멤법입니다.


name = ['영웅재중', '최강창민', '유노윤호', '시아준수', '믹키유천']
print('삭제전: ', name)
while True:
    print('삭제할 이름을 입력하세요!')
    rename = input('>')

    if rename in name:
        name.remove(rename)
        print('삭제후: ',name)
        break
    else:
        print('{}는(은) 없는 멤버입니다.'.format(name))









