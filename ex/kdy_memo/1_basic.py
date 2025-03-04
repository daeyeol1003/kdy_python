# %s 문자열 // %c 1개의 문자   //  %d 정수값  //  %f 실수
str1 = '100'
str2 = '200'
str3 = '12.345'

print(type(str1))
print(str1 == str)
int1 = int(str1)
print (int1 == int)

# format() 함수
# money = int(input('금액을 입력하세요 :'))
# print ('지갑에 있는 돈은 {}원입니다'.format(money))

# 집합 자료형
# 리스트, 튜블, 딕셔너리등으로 구성됨
# 여러개의 데이터를 처리하기 위한 자료형을 의미

# 리스트
somelist = ['곽대열','이승훈','한성우','이정호','이종찬','배상민','남신욱']
print(somelist)
print('1번째부터 3번째까지 출력')
# 슬라이싱
print(somelist[1:4])    # 종료 인덱스는 -1 처리되어 출력된다.
print(somelist[3:])   # 종료 인덱스가 없으면 끝까지 출력.

length = len(somelist)
print('홀수번째만 출력')
print(somelist[1:length:2])

# 튜플
# 튜플 생성하기
tuple01 = (10,20,30)
print(tuple01)
# 튜플요소 추가 방식
tuple01 = tuple01 + (40,)
print(tuple01)

tuple02 = 10,20,30,40

list = [10,20,30,40]
tuple03 = tuple(list)

if tuple02 == tuple03 :
    print('component equal')
else :
    print('component not equal')

tuple04 = 10,20,30
tuple05 = 40,50,60
tuple06 = tuple04 + tuple05
print(tuple06)
# 튜플 슬라이싱
print(tuple06[1:3])

# 딕셔너리
dictionary = {'김유신':50,'윤봉길':40,'김구':60}
print('dictionary.keys()')
for key in dictionary.keys():
    print(key)

print('dictionary.values()')
for value in dictionary.values():
    print(value)

print('\nkeys()를 이용한 value 검색하기')
for key in dictionary.keys():
    print('{}의 나이는 {}입니다'.format(key,dictionary[key]))

result = dictionary.pop('김구')
print(dictionary)
print(result)







