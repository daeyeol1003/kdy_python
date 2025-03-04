print("=== <<< 함수 >>> =====")

# 1. 문자열 삽입 -join()
str = ","
result = str.join('abcdefg')

print("result => ",result)

# 2. 양쪽 공백 제거 - strip()
str = "   happy    "
result = str.strip()
print("str => ",str)
print("result => ",result)

# 왼쪽 공백제거
l_result = str.lstrip()
print("l_result =>",l_result)

# 오른쪽 공백제거
r_result = str.rstrip()
print("r_result =>",r_result)

# 3.대문자를 소문자로 - Lower()
str = 'HI'
result = str.lower()
print(result)

# 4.소문자를 대문자로 - Upper()
str = 'hi'
result = str.upper()
print(result)

# 문장의 첫번째 문자를 대문자로 - capitalize()
str = 'have a good time'
result = str.capitalize()
print(result)

print("===== <<< 함수 작성 및 호출 >>> =====")
# 1. 함수를 작성하고 호출하기
def print_info():
    print("이름 :","김태희")
    print("이메일 : ","kth@mail.com")
    print("나이 : ",30)

# 함수 호출 : 함수명()
print_info()

print('-----------------')

# 2. 함수에 1개의 매개변수 전달하기
def print_info(name):
    print("이름 :", name)
    print("이메일 : ", "kth@mail.com")
    print("나이 : ", 30)
print_info(name="소지섭")

# 3. 함수에 여러개의 매개변수 전달하기.. 매개변수의 갯수는 값으 갯수와 정확히 일치해야한다.
# 1~10 까지의 합계 구하기
def cal_sum(start, end):
    sum = 0
    for i in range(start,end):
        sum += i
        print(sum)
cal_sum(1,11)

print()
print("=== <<< 객체 생성하기 >>> =====")

# 1. 객체의 설계도 작성
class Car:
    def drive(self):    # 메서드 - 메서드 첫번째 매게변수는 항상 self로서, 현재 객체를 가리킨다.
        self.speed = 10 # 속성

# 2. 객체 생성 - 기본생성자를 사용 -
# 자바 : 클래스명 참조변수 = new클래스명();
myCar = Car()   # 자바 Car myCar = new Car();

# 3. 객체의 속성 설정
myCar.name ="포르쉐911"
myCar.speed = 250
myCar.color = "red"
myCar.price = 250000000

# 4. 객체의 속성 출력
print("나의 자동차 정보 출력")
print("차 이름 :",myCar.name)
print("최고속도 :",myCar.speed)
print("차 색상 :",myCar.color)
print("차 가격 :",myCar.price)

# 5. 객체의 메서드 호출
# drive() 메서드의 self 매게변수(=자바의 this)는 어떤 객체가 메서드를 호출했는지 알려준다.
# 하지만 객체를 매개변수로 넣어서 drive()를 호출하지 않는다.
# drive() 메서드를 호출 할때는 항상 "객체이름.메서드명"과 같은 형식을 사용하며, 객체이름이 바로 self로 전달됨
myCar.drive()   # 참조변수.매서드명
print("drive 스피드 ",myCar.speed)

print('---------------------')

print("=== 입사 회사 출력 ===")
class Company:
    def com_info(self):
        self.salary = 3000
myCompany = Company()
myCompany.hiredate = "2025/12/31"
myCompany.salary = 4000
myCompany.kakao = "카카오"
myCompany.jejudo = "제주도"
myCompany.react = "리액트"

print("회사명 : ",myCompany.kakao  )
print("입사일 : ",myCompany.hiredate  )
print("연봉 : ",myCompany.com_info()  )
print("상승된 연봉 : ",myCompany.salary  )
print("회사 위치 : ",myCompany.jejudo  )
print("개발언어 ",myCompany.react  )

print()
print("=== <<< 객체 생성하면서 초기화하기 .. 매개변서 생성자를 사용 >>> =====")

# __init()__(self) => 기본생성자
# 1. 객체의 설계도 작성
class Member:
    # 매개변수 생성자
    def __init__(self,id,name,age,email,job):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.job = job
# 메서드
    def work(self):
        self.job = "progamer"

# 2. 객체 생성 - 매개변수 생성자를 사용

# 3. 객체의 속성 출력
print("=== member 정보 출력 ===")

member = Member("곽대열","dayeol","30","dayoul222@nate.com","rich")

print("=== member 정보 출력 ===")
print("id : ",member.id)
print("name : ",member.name)
print("name : ",member.age)
print("name : ",member.email)
print("name : ",member.job)

member.work()
print("메서드 work :",member.job)




