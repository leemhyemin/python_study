# 파일을 로딩하는 방법
file_path = 'D:/isec_Hmo3o/py_study/dddd.txt'

# encoding='utf-8 인코딩 한글 
try:
    f = open(file_path, 'r', encoding='utf-8')
    data = f.read() # read 한번에 다 불러냄 메모리 손상
    print(data)
except:
    print('파일 로드 실패!')
finally:
    f.close()

print('='*40)
try:
    f = open(file_path, 'r', encoding='utf-8')
    while True:
        str = f.readline()
        if len(str) == 0: break
        print(str, end='')

except:
    print('파일 로드 실패')
finally:
    f.close()