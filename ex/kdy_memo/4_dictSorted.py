wordInfo = {'세탁기':50,'선풍기':30,'청소기':40,'냉장고':60}

# 값의 크기가 큰 것부터 정렬한 후의 키를 반환합니다.
myticks = sorted(wordInfo, key=wordInfo.get, reverse=True)  # reverse 값이 True : 내림차순(역순) / False 이면 올림차순(정순)이다.
print(myticks)

# 키에 대하여 역순으로 정렬합니다. 이건 문제 없습니다. 키가 맞습니다.
reverse_key = sorted(wordInfo.keys(), reverse=True)
print(reverse_key)

# 값에 대하여 역순으로 정렬합니다.
chartdata = sorted(wordInfo.values(), reverse=True)
print(chartdata)