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
greeting = "Good Day~~~~"
print("인사 :", greeting)

print()

print("============= 사용자로부터 정수 입력받기 =============")
# input() 함수는 기본적으로 문자열을 입력받음 (자바의 scanner 기능)
# -> 숫자로 입력받으려면 int(), eval() 함수 사용
# x = int(input("첫 번째 정수를 입력하세요. : "))
# y = int(input("두 번째 정수를 입력하세요. : "))

# x + y의 합계 출력
sum = x + y
print(x, "+" , y, "=", sum)

print()

print("============= 카페 매출 계산하기 =============")
americano_price = 4000
cafelatte_price = 5000
hongsi_price = 6000

# 판매 개수 입력받기
americano_cnt = int(input("아메리카노 판매 개수를 입력하세요. : "))
cafelatte_cnt = int(input("카페라떼 판매 개수를 입력하세요. : "))
hongsi_cnt = int(input("홍시 판매 개수를 입력하세요. : "))

# 매출액 계산 = 각 음료 판매 개수 * 금액
americano_total = americano_cnt * americano_price
cafelatte_total = cafelatte_cnt*cafelatte_price
hongsi_total = hongsi_cnt*hongsi_price

total = americano_total + cafelatte_total + hongsi_total
print("총매출액 : ", total)

