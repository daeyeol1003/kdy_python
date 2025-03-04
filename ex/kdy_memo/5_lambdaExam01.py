# 일반 함수 동작
def nolambda(x,y):
    return 3 * x + 2 * y

x, y = 3, 5

result = nolambda(x,y)
print('일반 함수 방식 : {}'.format(result))

# 람다 함수
yeslambda = lambda x, y : 3*x + 2*y
result = yeslambda(x,y)
print('람다 방식 01 : {}'.format(result))

result=yeslambda(5,7)
print('람다 방식 02 : {}'.format(result))
