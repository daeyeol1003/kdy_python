print("===== <<< 2. 짝수 홀수 출력 >>> ======")
num = int(input("정수루 입력하세요:"))
if num%2 == 0:
    print("짝수")
else :
    print("홀수")

print("===== <<< 3. 다양한 조건을 판단하는 elif >>> =====")
tr = input('이동할 교통수단을 입력하세요 : ')
pocket =[tr,'money']

# pocket에 cellphone이 있으면 '카카오 택시탄다' 출력, card가 있으면 '카드내고 버스탄다' 출력, 그렇지않으면 '걸어간다'출력

if 'cellphone'in pocket:
    print("카카오 택시탄다")
elif 'card'in pocket:
    print("카드내고 버스탄다")
else :
    print("걸어간다")

print("===== <<< 4. 로그인 >>> =====")
# 아이디를 입력받아 해당 아이디가 일치하면 '환영합니다' 출력 | 일치하지않으면 '아이디 불일치' 출력
id = 'hong1234'
strId = input("아이디를 입력해 : ")
if strId == id:
    print("ㅎㅇ")
else :
    print("ㅂㅇ")