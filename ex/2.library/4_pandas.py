# Series(key, value) : 1차원 배열
# DaraFrame(테이블 형식) : 2차원 배열

import numpy as np
import  pandas as pd
from numpy.f2py.crackfortran import privatepattern
from pandas.core.config_init import pc_max_info_rows_doc

print("--- 1. 1차원 배열 - Series 자료형 생성(인덱스 없이) ---")
# 1차월 배열 - Series 자료형 생성
# 인덱스와 값 출력
# 인덱스 : 생략시 0,1,2,3.. 이며 숫자 문자 모두 가능

series_data = pd.Series([2,4,6,8,10])
print(series_data)

print("--- 2. 1차원 배열 - Series 자료형 생성(인덱스 부여) ---")
# 1차원 배열 - Series 자료형 생성
series_data = pd.Series([2,4,6,8,10],index=['a','b','c','d','e'])
print(series_data)

print("--- 3. 2차원 배열 - DataFrame 사용 (표현식) ---")
# 2차원 배열 - DataFrame 사용(표현식)
df = pd.DataFrame([[10,20,30],[40,50,60],[70,80,90]])
print(df)

print("--- 4-1. 전체 데이터 추출하기 ---")
# 원하는 데이터 추출하기
# Dictionary를 데이터 프레임으로 변환
# Dictionary는 {}로 감싸고, key-value로 되어있다.
# 5명의 키, 몸무게 유형 데이터 프레임생성하기

tbl = pd.DataFrame({
    "체중" : [50,60,70,80,90],
    "신장" : [150,160,170,180,190],
    "성별" : ["여","여","여","남","남"]
})
print(tbl)

print("---- 4-2. 원하는 데이터 추출하기 ---")
print(tbl["체중"])
print(tbl["신장"])
print(tbl["성별"])

print("---- 4-3. 원하는 데이터 추출하기 ---")
print(tbl[["체중","신장"]])

print("---- 4-4. 원하는 데이터 추출하기 ---")
print(tbl[tbl.성별 == "여"])

print("----- 5. Dictionary를 데이터 프레임으로 변환 -----")
# Dictionary => {key:value, key:value ....}
dic_data = {"names":["장효빈","김장민","김영석","김석균","김도영"],
            "years":[1992,1991,1990,1995,1993],
            "points":[1.5, 2.0, 2.5, 3.0, 3.5]
            }
df = pd.DataFrame(dic_data)
print(df)

print("----- 6-1. 데이터 프레임의 기본 통계 데이터 -----")
print(df.describe())
# std : 표준편차(=분산의 제곱근)이며, 값이 클수록 데이터가 떨어져있다.
# 분산 : 평균값에서 얼마나 떨어져있는지의 값
# 사분위수 : 4등급 .. 왼쪽 (25%) 가운데 (50%) 오른쪽 (75%)

print("--- 6-2. 데이터프레임의 값(인덱스, 컬럼값을 제외한 내용만 출력---")
print(df.values)

print("--- 6-3. 인덱스, 컬럼명 바꾸기---")
# 인덱스명 바꾸기
df.index.name = "Num"

# 컬럼명 바꾸기
df.columns.name = "Info"
print(df)

print("--- 7. Dictionary를 데이터프레임으로 변환---")
# Dictionary => {key:value, key:value ....}
# index : 인덱스 목록
# columns : 컬럼목록
df2 = pd.DataFrame(dic_data, columns=["names","years","points","penalty"], index=["A","B","C","D","E"])

# 표형태의 데이터 출력
print(df2)

print("--- 7-1. 값,인덱스 목록, 컬럼 목록 출력 ---")
print(df2.values)   # 값
print("df2.index => ",df2.index)   # 인덱스

print("--- 7-2. 데이터프레임의 일부 컬럼만 출력 ---")
print(df2["years"])

print(df2.years)

print("--- 7-3. 복수개의 열 ---")
print(df2[["years","points"]])

print("--- 7-4. Nan 필드에 값 대입 ---")
df2["penalty"] = 0.8
print(df2)

print("--- 7-5. Nan 필드에 각각 다른값 대입(우변에 리스트) ---")
df2["penalty"] = [0.5, 0.6, 0.7, 0.8, 0.9]
print(df2)

print("--- 7-6. 새로운 컬럼 추가 및 할당 ---")
df2["ages"] = np.arange(20,25)  # 파이썬의 range(범위)와 비슷 => 20~24
print(df2)

print("--- 7-7. 컬럼삭제 - del ---")
del df2["ages"]
print(df2)

print("--- 8-1. 특정행 조회 - loc[문자인덱스] / iloc[숫자인덱스]---")
print(df2.loc["E"])
print()

print(df2.iloc[2])

print("--- 8-2. 인덱스 범위 조회 - loc[문자인덱스]---")
print(df2.loc["A":"C"])

print("--- 8-3. loc[행범위,열범위] ---")
# loc[start : end, ] => 전체 행, 전체 열
# 전체행중에서 "names", "years" 필드만 추출
print(df2.loc[:,["names","years"]])

print("--- 8-4. 모든행의 1~3열---")
print(df2.iloc[:,1:4])      # 인덱스 0부터

print("--- 8-5. boolean 인덱싱  ---")
print(df2)
print()
# years가 2021보다 큰 데이터를 추출
print(df2["years"]>1990)    #거짓 : False, 참 : True

print("--- 8-6. True가 나온 행들만 추출 ---")
# Years가 1991보다 클때의 모든 열
# loc[행범위, 열범위]
print(df2.loc[df2["years"]>1991,:])

print("--- 9. 컬럼과 인덱스 설정후 시작일로부터 5일간 추출 ---")
# 컬럼명 지정
df2.columns = ["A","B","C","D"]

# 인덱스명 지정
df2.index =  pd.date_range("20241031",periods=5)     # 시작일로부터 5일간 출력
print(df2.index)
print()
print(df2)

