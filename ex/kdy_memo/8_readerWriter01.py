from numpy.ma.extras import average

print('파일을 읽기모드로 오픈.')
# open(파일이름,형식(읽기,쓰기),인코딩 문자열) 그 외의 여러 옵션 추가가능...
myfile01 = open('sample.txt','rt',encoding='UTF-8')
linelists = myfile01.readlines()
print(linelists)
myfile01.close()

total = 0  # 총점
for one in linelists :
    score = int(one)
    total += score

average = total / len(linelists)
print(total)
print(average)

print('파일을 쓰기 모드로 오픈한다.')
myfile02 = open('result.txt','wt',encoding='UTF-8')
myfile02.write('총점 :'+str(total)+'\n')
myfile02.write('평균 :'+str(average))

myfile02.close()
print('작업완료')









