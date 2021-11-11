# 영어단어장 만들기
# - 종료 하시려면 영단어에 "그만"을 입력하세요!
# 영단어:
# 뜻:
# 이미 등록된 단어입니다.
# 종료합니다.
# ***단어장 ***

print('[영어 단어장 만들기]')
print('- 종료하시려면 영단어에 "그만"을 입력하세요!')

word_dict = {}

while True:
    eng = input('\n영단어: ')

    if eng == '그만':
        print('종료합니다.')
        break

    
    if eng not in word_dict:
        kor = input('뜻: ')
        word_dict[eng] = kor;
    else:
        print('이미 등록된 단어입니다.')

        print('그만')
        continue

print('*** 단어장 ***')
for word in word_dict:
    print(f'{word} : {word_dict[word]}')
# print('*** 단어장 ***')
# for e in engdict:
#     count = engdict[eng]
#     print(f'# {eng} : {count}')


