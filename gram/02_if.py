a = input('a = ')
b = input('b = ')

if(a>b):
    print('zz')
elif(a==b):
    print('zzz')
else:
    print('zzzz')

print(a if a>b else b) # 삼항연산