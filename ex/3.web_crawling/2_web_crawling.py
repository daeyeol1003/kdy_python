from bs4 import BeautifulSoup

print("--- 2. BeautifulSoup --- ")
# BeautifulSoup : HTML 파싱 라이브러리 - 파싱 : 구문 분석, 구조 분석, 소스 코드 분석
# 사이트 : https://www.crummy.com/software/BeautifulSoup/
# pip install BeautifulSoup4 (파이참, Terminal, 아나콘다, 커맨드)

html = """
<html>
    <body>
        <h1> Hello </h1>
        <p> 웹 페이지 분석 </p>
        <p> 웹 스크래핑 </p>
    </body>
</html>
"""

# BeautifulSoup : Html 파싱 라이브러리
# html : 소스 텍스트
# "html.parser" : HTML 분석기
soup = BeautifulSoup(html, "html.parser")

# 원하는 부분 추출하기
h1 = soup.html.body.h1
p1 = soup.html.body.p

# next_sibling : 형제 요소를 가르침(공백 포함)
p2 = p1.next_sibling.next_sibling
p3 = p1.next_sibling

print("h1 = ", h1.string) # h1 = Hello
print("p1 = ", p1.string) # p1 = 웹페이지 분석
print("p2 = ", p2.string) # p2 = 웹 스크래핑
print("p3 = ", p3.string) # p3 = 공백

