from bs4 import BeautifulSoup


html = """
<html>
    <body>
        <div id="main">
        <h1> 도서목록 </h1>
        <ul class="items">
            <li>프로그래밍입문</li>
            <li>JSP</li>
            <li>스프링</li>
            <li>파이썬</li>
        </ul    
    </body>
</html>
"""

# BeautifulSoup으로 구문분석
soup = BeautifulSoup(html, "html.parser")

# 도서목록
h1 = soup.html.body.h1
print(h1)

# select_one : 중복 없는 1개의 태그가 가지고 있는 값 출력
h2 = soup.select_one("div#main > h1")
print(h2.string)

# select : 여러개 의 태그가 가지고 있는 값 출력
li = soup.select("li")
print(li)











