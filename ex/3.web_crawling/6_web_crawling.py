from urllib.request import urlopen
import  pandas
import pandas as pd
from bs4 import BeautifulSoup

# 기상청 날씨누리 - 생활기상지수

html = urlopen('https://www.weather.go.kr/w/resources/jsp/life/imgdata_popup.jsp?CODE=N07_2&point=0&nowchk=Y')  # 지점값보기

bsObject = BeautifulSoup(html,'html.parser')
df = pd.DataFrame(columns=['Region','Rate']) # [지점, 지수 단계]

# <table class="viewDataT> => table 하위 모든 정보 => find_add("table", {"class","viewDataT"})

table = bsObject.body.find_all("table", {"class","viewDataT"})
index = table[0]
trs = index.find_all("tr")

# 3행( 0행 날짜, 1행 타이틀 제외)부터 tr 행의 길이
for i in range(2,len(trs)):
    region = trs[i]
    ths = region.find_all('th', {'scope':'row'})
    tds = region.find_all('td')

    for j in range(0, len(ths)):
         df2 = pd.DataFrame({'Region':[ths[j].text],'Rate':[tds[j].text]})
         df = df._append(df2, ignore_index=True)
print(df)












