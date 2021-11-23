

'''
point.txt.를 읽어들여서
점수의 총점과 평균을 구한 후
총점과 평균을 적어서 resul.txt에 저장
'''

# 저장할 파일 resul.txt
try:
    f = open('D:/isec_Hmo3o/py_study/point.txt','r')
    point_str = f.read
    points = point_str.split(',')
    print(points)

    total = 0
    for n in points:
        total += int(n) #정수로 바꿔서 total에 누적
    avg = total / len(points)

except:
    print('파일 로드 실패')
finally:
    f.close()
import math
try:
    f = open('D:/isec_Hmo3o/py_study/result.txt','w')
    data = f'총점: {total}점, 평균: {round(avg, 2)}점'
    f.write(data)
except:
    print('파일 쓰기 실패')
finally:
    f.close()