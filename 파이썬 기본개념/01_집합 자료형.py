# 파이썬 용도
# 1. 수치연산처리 : 행렬 및 통게 연산을 수행하는 Numpy 수치 연산 모듈 제공
# 2. GUI 프로그래밍 : Tkinter(기본내장), wxPython, 등을 사용하여 화면에 창을 만들고 내부에 메뉴, 버튼 ,그림 등을 추가한 프로그램을 생성
# 3. 데이터베이스 프로그래밍 : Oracle, MySQL, PostgreSQL등의 RDBMS에 접근을 수행하기위한 도구 제공.
# 4. 네트워크 제어 : 네트워크 관련 모듈 사용하여 하드웨어 장치를 제어.
# 5. 웹 프로그래밍 : Flask 나 Django 등의 파이썬 웹 프레임워크를 사용하여 웹 사이트를 제작.
# 6. 빅 테이터 / 인공지능 : Pandas(데이터분석), Tensorflow,Keras (인공지능)등의 모듈 사용.
# 7. 텍스트 처리
from traceback import print_tb

# 주요 라이브러리
# 1. numpy (넘파이) : 배열을 사용하는, 수치 연산을 위한 라이브러리
# 2. pandas (판다스) : 데이터 분석
# 3. matplotlib (맷플롯립) : 데이터 시각화
# 4. beautifulsoup4 (뷰티풀 수프) : HTML/xml 등의 문서에서 데이터를 읽어옴
# 5. folium (포리움) : 지도를 그려주는 라이브러리

 # 포멧코드
 # %s(문자열), %c(1개의 문자), %d(정수), %f(실수)

 # ** 집합 자료형 **
# 리스트 [] : 순서가 있는 변경 가능한 데이터 구조, 중복된 값 저장 가능, 값 변경 가능

print('리스트 선언')
myList = []  # 빈 리스트 생성
numbers = [1,2,3,4,5] # 여러 개의 요소 포함 리스트
print('myList =>',myList)
print('numbers =>',numbers)
print('------------------------------')

print('리스트 주요기능 (메서드)')
print('리스트 요소 접근 (indexing & slicing')
numbers = [10,20,30,40,50]
print('numbers =>',numbers)
print('첫번째 요소 => ',numbers[0])
print('마지막 요소 =>',numbers[-1])
print('슬라이싱 => ',numbers[1:4])
print('------------------------------')

print('리스트 요소 추가(append, insert, extend)')
my_list = [1,2,3]
print('my_list => ',my_list)
my_list.append(4) # 리스트 끝에 추가
print(my_list)

my_list.insert(1,100) # 인덱스 1에 100 삽입
print(my_list)

my_list.extend([5,6,7])  # 여러 개의 요소 추가
print(my_list)
print('------------------------------')

print('리스트 요소 삭제 (remove, pop, del)')
fruits = ['apple','banana','cherry','banana']
fruits.remove('banana')  # 첫 번째로 만나는 'banana' 삭제
print(fruits)

fruits.pop(1)  # 인덱스 1의 요소 제거
print(fruits)

del fruits[0] # 특정 인덱스의 요소 제거
print(fruits)

# pop : 특정 인덱스 요소 삭제후 삭제된 요소 반환 , 리스트 전체 삭제 불가능
# del : 특정 인덱스 요소 삭제후 반환 x 리스트 전체 삭제 가능

print('------------------------------')
print('리스트 정렬(sort, reverse)')
num = [3,1,4,1,5,9,2]
print('num =>',num)

num.sort()  # 오름차순 정렬
print(num)

num.sort(reverse=True) # 내림차순 정렬
print(num)

# 원본 유지를 원하면 sorted() 사용
# ex) reveres_num = num.sorted(reveres=True)
print('------------------------------')

print('리스트 길이 확인 (len)')
my_list = [10,20,30,40]
print(len(my_list))

print('------------------------------')
print('리스트 활용 예시')
print('1. 리스트 컴프리헨션 (List Comprehension)')

# 1부터 10까지의 제곱 리스트 만들기
print('1부터 10까지의 제곱 리스트 만들기')
squares = [x**2 for x in range(1,11)]
print(squares)

print('2. 리스트 중복 제거')
nums = [1,2,2,3,4,4,5]
unique_nums = list(set(nums))
print(nums,'=>',unique_nums)

print('3. 리스트의 모든 요소 합 구하기')
numbers = [1,2,3,4,5]
print(numbers,'의 모든 합 =>',sum(numbers))
print('------------------------------')

# 튜플 () : 순서가 있고 값 변경이 불가능, 중복 값 저장 가능, 리스트 보다 속도가 빠름.

print('튜플 선언')
empty_tuple = ()   # 빈 튜플 생성
numbers = (1,2,3,4,5) # 여러 요소가 있는 튜블
single_element = (42,)  # 한개의 요소를 가진 튜플 ** 반드시 요소 뒤에 (,)가 있어야 한다.

print('빈 튜플 생성 =>',empty_tuple)
print('여러 요소가 있는 튜플 생성 =>',numbers)
print('한개의 요소를 가진 튜플 =>',single_element)
print('------------------------------')

print('튜플 요소 접근 (Indexing & Slicing)')
numbers = (10,20,30,40,50)
print(numbers)
print('첫번째 요소 => ',numbers[0])
print('마지막 요소 => ',numbers[-1])
print('슬라이싱 => ',numbers[1:4])
print('------------------------------')

print('튜플에서 요소 개수 세기 (count, index)')
fruits = ('apple','banana','cherry','banana')
print(fruits)
print('banana의 갯수 =>',fruits.count('banana'))
print('apple의 인덱스 =>',fruits.index('apple'))
print('------------------------------')

print('튜플 요소 합치기(연결(+), 반복(*))')
a = (1,2,3)
b = (4,5,6)
print('튜플 합치기 =>',a+b)
print('튜플 반복 =>',a*2)
print('------------------------------')

print('튜플 길이 확인(len)')
numbers = (10,20,30,40)
print(numbers)
print('numbers의 길이 =>',len(numbers))
print('------------------------------')

print('튜플을 리스트로 변환 (수정 하려면 변환이 필요)')
tup = (1,2,3)
lst = list(tup)  # 튜플 -> 리스트 변환
lst.append(4)  # 리스트에서 값 추가  튜플에선 추가x
tup = tuple(lst)  # 리스트 -> 튜플 변환
print(tup)
print('------------------------------')

print('튜플 활용 예시')
print('1. 여러 개의 값을 한 번에 반환')
def get_info():        # 함수 선언
    return 'Alice', 25, 'Developer'  # 튜플 반환
print(get_info())
name, age, job = get_info()     # 튜플 언패킹
print(name)
print(age)
print(job)
print('------------------------------')

print('2. 튜플 언패킹(값 여러 개 한 번에 할당)')
coordinates = (10,20)
x, y = coordinates
print(coordinates)
print(x)
print(y)
print('------------------------------')

print('3. 튜플을 이용한 값 교환')
a, b = 5,10
a, b = b, a
print(a,b)
print('------------------------------')

# 딕셔너리 {} : key와 value를 쌍으로 저장하는 데이터
# 순서가 없음, 키(key)를 통해 value접근,  중복된 key x, value는 중복가능
# 값 수정, 추가, 삭제 가능
# 키(key)는 불변 자료형 사용, 값은 자료형 제한 x

print('딕셔너리 선언')
# 빈 딕셔너리
empty_dict = {}
# 키와 값으로 딕셔러니 생성
person = {"name":"Alice","age":25,"job":"Developer"}

print('빈 딕셔너리 =>',empty_dict)
print('키와 값으로 딕셔러니 생성 =>',person)
print('------------------------------')

print('딕셔너리 기본 사용법')
# 딕셔너리에서는 키를 사용하여 값에 접근한다.
print('값 접근하기')
print('person["name"] =>',person["name"])
print('person["age"] =>',person["age"])
print()
# 키가 존재할때 발생하는 에러 방지를 위해 get() 메서드를 사용
# get() 메서드 사용시 키가 없으면 None을 반환한다.
print('get() 메서드 사용')
print('person.get("name") =>',person.get("name"))
print('person.get("address") =>',person.get("address"))
print()

print('키-값 수정하기')
person = {"name":"Alice","age":25}
# 키가 없으면 추가하고, 있으면 수정
person["job"] = "Developer"
person["age"] = 26

print(person)
print('------------------------------')

print('키-값 삭제하기')
person = {"name": "Alice", "age": 25, "job": "Developer"}

# 특정 키-값 삭제
del person["age"]

# pop()을 사용해서 삭제하고 그 값을 반환
remove_value = person.pop("job")

print(person)
print(remove_value)
print('------------------------------')

print('딕셔너리의 키와 값 모두 출력하기')
person = {"name": "Alice", "age": 25, "job": "Developer"}

#키만 출력
print('키만 출력 =>',person.keys())

#값만 출력
print('값만 출력 =>',person.values())

#키-값  출력
print('키-값 출력 =>',person.items())



# 비교 항목	    리스트 (List)	        튜플 (Tuple)	            딕셔너리 (Dictionary)
# 순서	        순서 있음 (인덱스 사용)	순서 있음 (인덱스 사용)	순서 없음 (키를 사용)
# 변경 가능	    변경 가능 (mutable)	    변경 불가능 (immutable)	변경 가능 (mutable)
# 중복	        중복 가능	            중복 가능	            키는 중복 불가 (값은 중복 가능)
# 접근 방법	    인덱스로 접근	            인덱스로 접근	            키로 접근