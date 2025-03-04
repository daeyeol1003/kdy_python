import urllib.request as req
from bs4 import BeautifulSoup

# 이미지 다운로드
print("--- 1. 구글 이미지 읽어서 저장 ---")
# 구글 사이트(http://www.google.com) 방문 -> 구글 로고 우클릭 -> 이미지 주소 복사 선택 -> 아래 url 변수에 붙여넣기
readur1 = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'  # input
savename = 'D:/DEV/workspace_python/data/images/google_logo.png'    # output

# 다운로드
# 다운로드 받은 이미지파일을 메모리에 저장
# 1) 구글로고를 읽는다.
g_image = req.urlopen(readur1).read()

# 2) 파일로 저장
# wb : write Binary
with open(savename, mode='wb') as f:
    f.write(g_image)
    print("구글 이미지가 저장되었습니다.!!") # 3) 메세지














