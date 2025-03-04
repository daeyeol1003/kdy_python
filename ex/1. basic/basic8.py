print("===== <<< 튜플 >>> =====")

# 1. 튜플이란?
# 리스트는 대괄호[]로 감싸고, 튜플은 소괄호()로 감싼다
# 리스트는 수정, 삭제가 가능하지만, 튜플은 수정,삭제가 되지 않으므로 변경안할 경우 사용
# 튜플은 tuple1 = (1,)처럼 1개의 요소만을 가질때는 요소뒤에 콤마(,)를 반드시 붙인다.
# 튜플은 tuple2 = 1,2,3 처럼 괄호()를 생각해도 무방하다.

tuple1 = () # 생성
tuple2 = (1,)
tuple3 = (1,2,3)
tuple4 = (1,2,3,('ab',),('cd',))
tuple5 = (1,2,'a','b')
tuple6 = 1,2,3

print("tuple1 =>",tuple1)
print("tuple2 =>",tuple2)
print("tuple3 =>",tuple3)
print("tuple3[0] =>",tuple3[0])
print("tuple3[1] =>",tuple3[1])
print("tuple3[2] =>",tuple3[2])
print("tuple4 =>",tuple4)
print("tuple5 =>",tuple5)
print("tuple6 =>",tuple6)

# 튜플은 수정,삭제가 되지 않으므로 변경안할 경우 사용
# tuple3[0] = 5
print("tuple3[0] =>",tuple3[0])
print()

# 2. 리스트의 요소가 튜플인 경우
list = [(1,2),(3,4),(5,6),(7,8),(9,10)]
for(first,second)in list:
    print(first+second)
    print("{0}+{1}={2}".format(first,second,first+second))

# 3. 튜플 인덱싱
tuple1 = (1,2,'a','b')
print("tuple1 =>",tuple1)
print("tuple1[1:] =>",tuple1[1:])

tuple2 = (3,4)
print("tuple1+tuple2 =>",tuple1+tuple2)

print("tuple2 * 3 =>",tuple2*3)

