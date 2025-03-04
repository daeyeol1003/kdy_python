from pyparsing import replaceWith

print("----- <<< numpy >>> -----")

# numpy
# 가. numpy 기본
# 1) 백터 및 행렬 연산에 특화된 라이브러리
# 2) array 단위로 데이터를 관리함, 행렬(matrix)과 비슷함
# 3) pandas와 함께 데이터분석에 많이 사용됨

import numpy as np

# 파이썬 리스트
print('파이썬 리스트')
data1 = [1,2,3,4,5]
print(data1)

# 리스트를 넘파이 배열로 변환
print('리스트를 넘파이 배열로 변환')
arr1 = np.array(data1)
print(arr1)

# 넘파이 배열의 크기
print('넘파이 배열의 크기')
print(arr1.shape)

# 2차원 리스트
print('2차원 리스트')
data2 = [[1,2,3],[4,5,6]]
print(data2)

# 2차원 리스트를 넘파이 배열로 변환
print('2차원 리스트를 넘파이 배열로 변환')
arr2 = np.array(data2)
print(arr2)

print("----- 5행 4열의 넘파이 배열의 전체합계, 평균 -----")
arr = np.random.rand(5,4)
print(arr)

# 전체 합계
print("전체 합계 : ", arr.sum())

# 전체 평균
print("전체 평균 :",arr.mean())

# 각 열(컬럼)의 합계 => aixs=0 => 열, axis=1 => 행
colSum = arr.sum(axis=0)
print(colSum)

rowSum = arr.sum(axis=1)
print(rowSum)