file01 = open('sample03.txt','rt',encoding='UTF-8')
filelist01 = file01.readlines()

for idx, line in filelist01:
    data = line.strip().split()
    if idx == 0:
        continue
    name = data[0]

