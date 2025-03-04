print("===== <<< if-else >>> =====")
# if 조건문 뒤에는 반드시 클론(:)을 붙인다.
# 클론(:) => 다음 문장과 연결됨을 의미하며, 다음문장은 반드시 들여쓰기(탭, 스페이스바 4칸)를 하지않으면 문법오류 발생

# if 조건문 : # 조건문에 ()를 사용하면 구문오류
# ....수행할 문장1 # 들여쓰기를 안하면 구문 오류
# ....수행한 문장2 # 들여쓰기를 안하면 구문 오류
# else :
# ....수행할 문장1 # 들여쓰기를 안하면 구문 오류
# ....수행할 문장2 # 들여쓰기를 안하면 구문 오류

# print("===== <<< 1. 성적 출력 >>> ======")
# score = int(input("성적을 입력하세요:"))
#
# # 60점 이상이면 합격, 그렇지 않으면 불합격
# if score >= 60 :
#     print("합격")
# else :
#     print("불합격")

# 이름(name), 국(kor),영(eng),수(math) 입력받아서 총점과 평균(avg), 학점(grade)을 구하고 모두 출력하시오.
name = input("이름을 입력하세요. :")
kor = int(input("국어점수를 입력하세요. :"))
eng = int(input("영어점수를 입력하세요. :"))
math = int(input("수학점수를 입력하세요. :"))

total = kor + eng + math
avg = float(total / 3)
print("총점 : ",total)
print("평군 :", avg)
if avg >=90:
    grade = "A학점"
elif avg >=80:
    grade = "B학점"
elif avg >=70:
    grade = "C학점"
elif avg >=60:
    grade = "D학점"
else :
    grade = "사람임?"
print("학점 :",grade)
