
'''
x = input('>> ').split()
for i in range(len(x)):
   x[i] = int(x[i])
print(x)
'''  
#파이썬에서만 지원하는것 여러개 입력 띄어쓰기
x = list(map(int, input('>> ').split()))
x.sort(reverse=True)
print(x)


