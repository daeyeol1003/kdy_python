# print("===== <<< for문 : 횟수 제어 반복 >>> =====")
# print("===== <<< 1. for문 >>> =====")
# # 1. for문
# # for 변수 in 리스트(또는 튜플, 문자열):
# # ....수행할 문장1
# # ....수행할 문장2
#
# for i in[1,2,3,4,5,6,7,8]:
#     print(i,"교시 시작")
#
# print()
#
# test = ['one','two','three','four','five']
# for i in test:
#     print(i,end=" ")
#
# print("===== <<< 2. range문 : 반복횟수가 큰 경우 >>> =====")
# # 2-1. for문 range() : 반복횟수가 큰 경우
# # for 변수 in range(start, end, step) # start 생략시 0, end -1, step 생략시 1
# # .... 수행할 문장1
# # .... 수행할 문장2
# for i in range(1,9):
#     print(i,"교시 시작~~")
#
# # 2-2. 10~1 값 한줄로 표현
# for i in range(10,0,-1):
#     print(i,end=" ")
#
print()
print("===== <<< 3. 2중 for문 >>> =====")
# for문 range()를 이용해서 구구단 출력
# 2단 ~ 9단, 단이 바뀔때마다 빈줄
# for 변수 in range(start, end, step)
for i in range(2,10):
    print()
    for j in range(1,10):
        print(i,"*",j,"=",i*j)

# print("===== <<< while문 >>> =====")
# # 1. while 조건문
# # while 조건문:
# # ....수행할 문장1
# # ....수행할 문장2
#
# # 1-1. while 1~10까지의 합계
# count = 1
# sum = 0
# while count <= 10:
#     sum += count
#     count += 1
#
# print("sum = ",sum)
#
# # 1-2. while - 로그인
# # password가 "python" => '로그인 성공' 출력, 비밀번호 출력
# # 그렇지 않으면 계속 입력
# password = input("비밀번호를 입력하세요 :")
# while password != "python":
#     password = input("다시 입력하세요 : ")
# else :
#     print("로그인성공")
#     print("password :",password)

# 1-3. while - break
# 구구단 출력
# 원하는 단은?(종료:0) 빠져나갈때 break
# True인 동안 무한루프, break를 만나면 빠져나간다.   (True T는 대문자여야 구문 오류 안남)

while True:
    dan = int(input("단을 입력하세요(종료:0) :"))
    if dan == 0:
        print("종료됩니다...")
        break
    for i in range(1,10):
        # print(dan,"+",i,"=",dan*i)
        print("%d * %d = %d"%(dan,i,dan*i))


# 1-4. while - continue => 스킵
# 1~10 까지의 홀수값 출력
num = 0
while num<10:
    num = num+1
    if num % 2 == 0:
        continue
    print(num)