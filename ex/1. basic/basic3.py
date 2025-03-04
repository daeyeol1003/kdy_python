from cgi import print_environ_usage

print("===== <<< 문자열 포맷팅 >>> =====")
# %d, %s, %c, %f : 문자열 포맷코드
# 문자열.format(변수)

# 1. 숫자 바로 대입
str1 = "I eat %d hamburgers."%3
print("str1 => ",str1)
# 2. 문자열 바로 대입
str2 = "I eat %s hamburgers."%"five"
print("str2 => ",str2)
# 3. 2개 이상의 값 넣기
number = 10
day = "four"
str3 = "I ead %d hamburger, for %s days"%(number,day)
print(str3)
# 4. 문자열.format(변수)
number = 2
str4 = "I eat {0} hamburgers.".format(number)
print(str4)

number = 12
day = 3
str5 = "I eat {0} hamburger, for {1} days.".format(number,day)
print(str5)

# 5. {인덱스} 대신 {변수명} 사용가능
str6 = "이름 : {name}, 나이{age}세 입니다.".format(name="홍길동",age=50)
print("str6 => ", str6)
print()

# 6. 천단위 콤바
num = 123456789
print("천단위 콤바")
print("{0:}".format(num))
print("{0:,}".format(num))

# 7. 백분율
print("백분율")
fnum = 0.6789
print("{0:0%}".format(fnum))
print("{0:.0%}".format(fnum)) # 소수점 이하 자리수 0
print("{0:.1%}".format(fnum)) # 소수점 이하 자리수 1
