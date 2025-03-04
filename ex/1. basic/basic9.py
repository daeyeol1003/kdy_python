print("===== <<< 딕셔너리 >>> ======")

# 키-값 쌍으로 구성, 중괄호{}로 생성, cj) 리스트는 대괄호[], 튜플은 소괄호()
# 예) 영어사전 - 단어(key), 단어설명(value)

print("===== 1. 생성후 초기화 =====")
# 1-1. 생성후 초기화
phone_book = {} #딕셔너리 생성

phone_book["현빈"]="010-1111-1111"    # 초기화 => 딕셔너리명["key"]="value"
phone_book["손예진"]="010-2222-2222"    # 초기화 => 딕셔너리명["key"]="value"
print(phone_book)

# 1-2. key를 이용해서 값을 읽어옴
print("phone_book['현빈'] =>",phone_book["현빈"])
print("phone_book['손예진'] =>",phone_book["손예진"])

# 1-3. key들을 읽어옴
print("keys =>",phone_book.keys())

# 1-4. value들을 읽어옴
print("values =>",phone_book.values())

print("===== <<< 2. 생성과 동시에 초기화 >>> =====")
# 2-1. 생성과 동시에 초기화
phone_book ={"유재석":"010-7777-7777"}
# 2-2. key들을 읽어옴
print("keys =>",phone_book.keys())

# 2-3. value들을 읽어옴
print("values =>",phone_book.values())

print("===== <<< 3. 삭제 >>> =====")
# 3-1. 디셔너리 삭제 = del
del phone_book["유재석"]
print(phone_book)
print()

# 3-2. 딕셔너리 전부 삭제 - clear
phone_book["현빈"]="010-1111-1111"
phone_book["손예진"]="010-2222-2222"
print("phone_book => ",phone_book)

phone_book.clear()
print("phone_book => ",phone_book)

print("===== <<< 4. 딕셔너리 추가 >>> =====")
# 4. 새로운 요소 추가 => 딕셔너리[key] = value
address = {1:'서울시 강남구'}
print("address => ",address)
address[2]='서울시 마포구'
address[3]='서울시 광진구'
print("address => ",address)

print("===== <<< 5. key로 value값 읽기(get) >>> ======")
info = {"name":"김태희","phone":"010-5555-5555","birth":"20200202"}
print("info => ",info)
print("info['name'] => ",info['name'])
print("info['name'] => ",info.get('name'))

print("info['phone'] => ",info['phone'])
print("info.get('phone') => ",info.get('phone'))

print("info['birth'] => ",info['birth'])
print("info.get('birth') => ",info.get('birth'))


# key들을 읽어옴
print("keys =>",info.keys())

# value들을 읽어옴
print("values =>",info.values())

print("===== <<< 6. for문으로 출력 >>> =====")
member = {"name":"김태희","phone":"010-5555-5555","birth":"20200202"}

# for 개별값 in 집합
for key in member.keys():
    print(key, end=" ")
print()
for values in member.values():
    print(values, end=" ")
print()
# keys 객체를 튜플로 생성
tuple1 = tuple(member.keys())
print("tuple1 => ",tuple1)

print("===== <<< 7. 딕셔너리의 아이템 >>> =====")
# 7-1. 딕셔너리의 아이템
print(type(member))
print(type(member.items()))
print("member.items() =>",member.items())

# 7-2. 딕셔너리의 아이템 응용
# 편의점 재고관리
gs = {'milk':5,'chocolate':4,'jelly':3,'nuddle':2,'potato':1}
item = input("물건의 이름을 입력해라 : ")
print(item,"의 재고수량은",gs[item],"입니다")



