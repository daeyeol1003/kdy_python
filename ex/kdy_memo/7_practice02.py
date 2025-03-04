# 제품명(name), 채널번호(channel), 소리크기(volume) 정보를 가지는 '텔레비전' 이라는
# 이름의 클래스를 구현
class Television:
    def __init__(self,name,channel,volume):
        self.name = name
        self.channel = channel
        self.volume = volume

    def info(self):

        return 'Tv이름 : %s'%self.name + '\n채널 : %d'%self.channel + '\n볼륨 : %d'%self.volume

name = input('Tv 이름을 입력하세요: ')
channel = int(input('채널을 입력하세요: '))
volume = int(input('볼륨을 입력하세요: '))

tv = Television(name,channel,volume)
print(tv.info())

# 두개 정수에 대하여 앞의 숫자에는 3제곱, 뒤의 숫자에는 더하기 2를 수행한 후, 최종적으로 앞의 숫자에서 뒤의 숫자를 뺄셈해주는 lambda 함수
newlambda = lambda x,y: x**3 - (y+2)
result = newlambda(3,5)
print('람다 : ',result)










