# 데이터 분석 실습 - 영화 평점 데이터
# 영화평점 데이터셋 로딩
# https://grouplens.org/datasets/movielens/
# older datasets > MovieLens 1M Dataset > ml-1m.zip 다운로드
# D:\Dev03\workspace_python_ict04\data\3.movie\ml-1m\ratings.dat

# 노트패드 다운로드 : 구글에서 노트패드 검색 > [notepad++ 다운로드] 클릭 > v8.7.6선택 해서
# Download 64-bit x64 > installer 클릭 > exe 파일 디폴트 설치

# ratings.dat 구조 => 노트패드 실행 > File > open
# ratings.dat 구조 => 6040::1097::4::956715569 => 사용자ID::영화번호::평점::시간

import numpy as np
# no.loadTxt => 아나콘다에서 작동(o), 파이참에서 작동(x)

movieData = np.genfromtxt("D:/DEV/workspace_python/data/3.movie/ml-1m/ratings.dat",
              delimiter="::",dtype=np.int64,encoding="utf-8")
# print(movieData)

# 데이터의 첫 5행, 모든 열 조회
# 넘파이배열[행범위,열범위]
# [start:end, start:end]
print("----- 데이터의 첫 5행, 모든 열 조회")
print(movieData[:5, :])

print("----- 데이터의 형태 확인 -----")
# 데이터의 형태확인
print((movieData.shape))   #(행갯수,열갯수)

print("----- 전체 평점에 대한 평균 계산 -----")
# 전체 평점 평균 계산
mean_rating = movieData[:,2].mean()
print(mean_rating)

print("----- 사용자 아이디 수집 -----")
# 사용자 아이디 수집
# 중복값 제거 : unique(대표값)
user_ids = np.unique(movieData[:,0])
print(user_ids)

print("----- 사용자별 평점 평균 집계 -----")
# 사용자별 평점 평균 집계
# 사용자별 평점 평균값을 저장할 배열
mean_values = []
for user_id in user_ids:
    # 해당 사용자 id의 모든 정보
    data_for_user =  movieData[movieData[:,0]== user_id,:]

    # 2번째 인덱스(평점)에 해당하는 값의 평균값
    mean_rating = data_for_user[:,2].mean()

    # 사용자 아이디와 평점평균값을 배열에 추가
    mean_values.append([user_id,mean_rating])

print("----- 사용자 아이디별 평점 평균[id, 평점]-----")
print(mean_values[:5])

mean_array = np.array(mean_values, dtype=np.float32)
print(mean_array)
print("----- 마지막 id인 6040행 2열(id,평점평균)의 넘파이 배열 -----")
print(mean_array.shape)
print("----- 넘파이 배열을 CSV 파일로 저장 => result 폴더 생성 > 6040건 성공 -----")
np.savetxt("D:/DEV/workspace_python/data/3.movie/ml-1m/result/ratings_result.csv",
            mean_array, fmt="%.1f",delimiter=",")   # result 폴더에 결과파일 자동 생성 => 결과확인 : 파일 우클릭 > 'Note++로 편집' 클릭