

inch = 2.54 # 1인치ㅏ에 대한 cm값 저장

# 인치를 cm으로 변환해주는 함수
def convert_inch_to_cm(numver):
    return numver * inch

def info():
    print('안녕~~ 메롱!!')

print('__name__의 값(custom.py):', __name__) #커스텀ㅁ

# 실행테스트
if __name__== '__main__':

    print('__name__의 값(custom.py):', __name__)


    print(convert_inch_to_cm(1))
    info()
    info()
    info()
    info()
    info()