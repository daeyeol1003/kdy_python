import os

myfolder = 'd:\\'

newpath = os.path.join(myfolder, 'hello')
# 새로운 폴더를 생성할때 이미 디렉터리가 존재하면 FileExistsError라는 예외가 발생하기에, 예외처리를 수행해야함
print('hello 폴더 생성 완료')

try:
    os.mkdir(path=newpath)

    for idx in range(1,11):
        newfile = os.path.join(newpath,'somefolder' +str(idx).zfill(2))
        os.mkdir(path=newfile)
except FileExistsError :
    print('디렉터리가 이미 존재합니다.')

print('finished')