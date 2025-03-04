# json 분석

import json

# json => {key:value, key:value}    # 파이썬의 딕셔너리와 형식이 동일

str = '{"amount":[{"num":0},{"num":1},{"num":2}],\
        "fruits":[{"fruits":"banana"},{"fruits":"mango"},{"fruits":"apple"}]}'

obj = json.loads(str)     # loads() : 파일이나 url에서 데이터를 읽어온다.

# json객체.get("key") => value를 읽어온다.
print(obj.get("fruits"))
print(obj.get("fruits")[0])
print(obj.get("fruits")[1])
print(obj.get("fruits")[2])
print()

print(obj.get("amount")[0])
print(obj.get("amount")[1])
print(obj.get("amount")[2])
print()

print(obj.get("amount")[0].get("num"))
print(obj.get("amount")[1].get("num"))
print(obj.get("amount")[2].get("num"))









