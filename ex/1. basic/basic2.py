from cgi import print_environ_usage

print("============= 자료형 =============")

# 자료형을 변수에 붙이지 않는다.
# 주석 단축키 : ctrl + /
# 들여쓰기 주의! : 조건문없을 때 들여쓰기해서 코드를 작성하면 에러 발생
# 실행 : 맨위 Current File로 바꾸고 run 버튼 (ctrl shift f10 / ctrl f5)
# 파이썬은 대소문자 구별함
a = 10
print("a =", a)   # a 값 출력

# 자료형 (정수, 실수, 문자열, 복소수, 8진수, 16진수)
# 복소수 : 실수부 + 허수부 => 실수부(실수 또는 정수) + 허수부(정수에 j 또는 J)
# 오른쪽의 값이 왼쪽 변수에 대입되는 시점으로 자료형이 결정된다.
x = 100
print("x =", x)   # x 값 출력

y = 3.14
print("y =", y)

z = "파이썬"
print("x =", x)

x += 1
print("x =", x)   # x 값 출력

# 문자열 출력

# x의 y 제곱근을 나타내는 ** 연산자
x = 3
y = 2
print("x**y =", x**y)  # 3의 2제곱근 | 9

# 나눗셈 /, //
# // : 소수점 이하 자릿수를 버린다. 정수형으로 값 반환 (반올림과 무관)
print("10 / 7 =", 10 / 7)
print("10 / 6 =", 10 / 6)
print("10 / 5 =", 10 / 5)

print()

print("10 // 7 =", 10 // 7)
print("10 // 6 =", 10 // 6)
print("10 // 5 =", 10 // 5)

print()
print("===== <<< 줄 바꾸기 >>> =====")
# 줄바꾸기
# \n,  연속된 작은 따옴표 3개(``` ```) , 연속된 큰 따옴표 3개(""" """)
multiline = "Life is too short. So you have to study hard!!"
print("multiline = ",multiline)
print()

multiline2 = '''Life is too short. 
So you have to study hard!!'''
print(multiline2)
print()

multiline3 = """Life is too short. 
So you have to study hard!!"""
print(multiline3)
print()

multiline4 = "Life is too short. \nSo you have to study hard!!"
print(multiline4)
print()

print("===== <<< 문자열 연산하기 >>> =====")
# 문자열 연산하기
# 문자열 더하기
head = "python"
tail = " is fun!!"
print(head + tail)

# 문자열 곱하기
str = "python "
print(str *3)

li = "="
print(li * 300)
print()

print("===== <<< 문자열 인덱싱과 슬라이싱(중요) >>> =====")
# 문자열 인덱싱과 슬라이싱
# 파이썬의 인덱싱 : 0부터 시작

str = "Nice Day"
print("str[4] =>",str[4])
print("str[5] =>",str[7])

# 슬라이싱(중요)
# str[시작번호 : 끝번호] => 시작번호 : 끝번호 -1
print("str[0:7] => ",str[0:8])

# 끝번호를 생략하면 시작번호부터 그 문자열의 끝까지 추출한다.
# So you have to study hard!!
print(str[3:])









