import  pandas as pd
import matplotlib.pyplot as plt
from cgi import print_environ_usage

from fontTools.misc.arrayTools import pointInRect
from numpy.ma.extras import average

even = [2,4,6,8,10]

even.append(12)
even.remove(10)
even.insert(0,1)
print(even)
#
# name = input("이름을 입력하세요:")
# kor = int(input("국어점수를 입력하세요:"))
# eng = int(input("영어점수를 입력하세요:"))
# math = int(input("수학점수를 입력하세요:"))
# total = kor + eng + math
# avg = total/3
# if(avg>90):
#     grade = "A학점"
# elif(avg>80):
#     grade = "B학점"
# elif(avg>70):
#     grade = "C학점"
#
# print("총점 :",total)
# print("평균 :",avg)
# print("학점 :",grade)
# print()

t_dic = {"name" : "hong", "phone":"010-9797-7979", "addr":"seoul" , "age" : 24}

for key, value in t_dic.items():
    print(f"{key}: {value}")

import pandas as pd



m_dict = [
    {'id': 1010, 'name': '마루치', 'Java': 89, 'Python': 78, 'Flask': 90},
    {'id': 1230, 'name': '아라치', 'Java': 96, 'Python': 80, 'Flask': 92},
    {'id': 1902, 'name': '을불', 'Java': 90, 'Python': 74, 'Flask': 90},
    {'id': 2002, 'name': '창조리', 'Java': 98, 'Python': 88, 'Flask': 94}
]

# 데이터프레임 생성
df = pd.DataFrame(m_dict)


totals = []
averages = []
grades = []

# 학점 계산
def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


# for문을 사용하여 총점, 평균, 학점 계산
for i in range(len(df)):
    java = df.loc[i, 'Java']  # Java 점수
    python = df.loc[i, 'Python']  # Python 점수
    flask = df.loc[i, 'Flask']  # Flask 점수

    total = java + python + flask
    average = total / 3
    grade = get_grade(average)

    totals.append(total)
    averages.append(average)
    grades.append(grade)


df['Total'] = totals
df['Average'] = averages
df['Grade'] = grades

print(df)

import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
names = ["Python","Java","Spring","React"]
score = [95,85,75,90]
ax1.plot(names,score,color="#f00")
ax1.bar(names,score)
ax1.set_title("sample")
ax1.set_xlabel("class")
ax1.set_ylabel("count")
plt.show()