

rnrn = int(input('국어:'))
dndn = int(input('영어:'))
tntn = int(input('수학:'))

avg = (rnrn + dndn + tntn) /3 
print('당신의 평균점수: {:.2f}점'.format(avg))

if avg >= 60: 
    print('이번 시험에 통과하셨습니다.')
else:
    print('재수강 대상자 입니다.')
print('열공하세요!')


