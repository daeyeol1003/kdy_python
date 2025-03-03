# 문자열 조작 관련 함수
print('1. 문자열 길이 구하기')
text = 'Hello, world!'
print('len(text) => ',len(text))  # 공백도 문자로 취급된다.
print('------------------------------\n')

print('2. 문자열 대소문자 변환')
text = "hello"
text2 = "hello world"
print('문자열 전체를 대문자로 변환 =>',text.upper())
print('문자열 전체를 소문자로 변환 =>',text.lower())
print('첫 번째 문자만 대문자, 나머지는 소문자로 변환 =>',text.capitalize())
print('각 단어의 첫 글자를 대문자로 변환 =>',text2.title())
print('------------------------------\n')

print('3. 문자열 공백 처리')
text = " hello world "
print('text.strip() : 문자열 양쪽 끝에 있는 공백 제거 =>',text.strip())
print('text.lstrip() : 문자열 왼쪽 끝 공백만 제거 =>',text.lstrip())
print('text.rstrip() : 문자열 오른쪽 끝 공백만 제거 =>',text.rstrip())
print('------------------------------\n')

print('4. 문자열 찾기 및 교체')
text = "hello world"
# find() : 문자열에서 특장 문자가 처음 등장하는 인덱스를 반환.  없으면 -1 반환
print('find()')
print(text.find("world"))
print(text.find("python"))

# index() : find() 와 비슷하지만, 문자열이 없으면 ValueError 발생
print('index()')
print(text.index("world"))
# print(text.index("python"))  # ValueError: substring not found

# replace() : 문자열 내에서 특정 부분을 다른 문자열로 교체
print('replace()')
print(text.replace("world","python"))

