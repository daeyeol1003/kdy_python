from http.client import responses
from os import access  # 657442516472686b3436796c58654b
# <?xml version="1.0" encoding="ISO-8859-15"?><rentBikeStatus><rentBikeStatus><list_total_count>5</list_total_count>
#  <row><shared>167</shared><stationLatitude>37.55564880</stationLatitude><stationLongitude>126.91062927 </stationLongitude><stationName>102. 망원역 1번출구 앞</stationName><parkingBikeTotCnt>25</parkingBikeTotCnt><rackTotCnt>15</rackTotCnt><stationId>ST-4</stationId></row>
#  <row><shared>150</shared><stationLatitude>37.55495071</stationLatitude><stationLongitude>126.91083527</stationLongitude><stationName>103. 망원역 2번출구 앞</stationName><parkingBikeTotCnt>21</parkingBikeTotCnt><rackTotCnt>14</rackTotCnt><stationId>ST-5</stationId></row>
#  <row><shared>177</shared><stationLatitude>37.55073929</stationLatitude><stationLongitude>126.91508484</stationLongitude><stationName>104. 합정역 1번출구 앞</stationName><parkingBikeTotCnt>23</parkingBikeTotCnt><rackTotCnt>13</rackTotCnt><stationId>ST-6</stationId></row>
#  <row><shared>140</shared><stationLatitude>37.55000687</stationLatitude><stationLongitude>126.91482544</stationLongitude><stationName>105. 합정역 5번출구 앞</stationName><parkingBikeTotCnt>7</parkingBikeTotCnt><rackTotCnt>5</rackTotCnt><stationId>ST-7</stationId></row>
#  <row><shared>92</shared><stationLatitude>37.54864502</stationLatitude><stationLongitude>126.91282654</stationLongitude><stationName>106. 합정역 7번출구 앞</stationName><parkingBikeTotCnt>11</parkingBikeTotCnt><rackTotCnt>12</rackTotCnt><stationId>ST-8</stationId></row>
#  <RESULT><MESSAGE>정상 처리되었습니다.</MESSAGE><CODE>INFO-000</CODE></RESULT></rentBikeStatus></rentBikeStatus>

# from craw.test import  totallist, beginRow

accessToken = '657442516472686b3436796c58654b'
pageSize= 1000
import pandas as pd
import requests
import numpy as np
from itertools import count

totallist = list()

for pageNumber in count():      # 데이터가 몇페이지까지 있는지 모를때 count()를 돌린뒤 예외처리에서 빠져나간다.
    beginRow = str(1+(pageNumber*pageSize))
    endRow = str(pageSize *(pageNumber + 1 ))
    url = 'http://openapi.seoul.go.kr:8088/'
    url += accessToken
    url += '/json/bikeList/'
    url += beginRow + '/'
    url += endRow + '/'
    print(url)


    # get(url)
    response = requests.get(url)
    jsondata = response.json()

    try :
        datalist = jsondata['rentBikeStatus']['row']
        for data in datalist:
            totallist.append(data)
    except Exception as err:
        print('Read END..')
        print(err)
        break

# xml 공공데이터 -> csv로 변환
# xml 공공데이터를 읽어서 아래 폴더에 새로 저장(이미 존재하는 경우는 삭제)
filename = 'D:/DEV/workspace_python/data/bike/2025_bikeList.csv'
myFrame = pd.DataFrame(totallist)
myFrame.to_csv(filename)
print(myFrame)

# 한글이 꺠진경우 > .csv 우클릭 > 연결프로그램 : 메모장 > 다른이름으로 저장 : UTF-8(BOM)으로 바꾼후 저장