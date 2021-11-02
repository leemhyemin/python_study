

print('***** 꽃을 선택하세요. *****')
print('[장미, 튤립, 백합, 안개꽃, 수선화]')

flower = input ('>')

if flower == '장미':
    print('{}의 가격은 5000원 입니다.'.format(flower))
elif flower == '튤립':
    print('{}의 가격은 5700원 입니다.'.format(flower))
elif flower == '백합':
    print('{}의 가격은 6000원 입니다.'.format(flower))
elif flower == '안개꽃':
    print('{}의 가격은 8000원 입니다.'.format(flower))
elif flower == '수선화':
    print('{}의 가격은 10000원 입니다.'.format(flower))
else:
    print(f'{flower}은/는 없습니다.')


