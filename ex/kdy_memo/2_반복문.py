# while 문
coffee = 3
price = 2000
while True:
    money = int(input('돈을 넣어주세요 : '))
    if money == price:
        print('커피를 팝니다.')
        coffee -=1
    elif money > price:
        count =  int(money / price)
        if coffee >= count:
            print('{}잔의 커피를 구매합니다'.format(count))
            coffee -= count
            if money-(count*coffee) > 0:
                print('거스름돈은 {}원 입니다'.format(money-(count*price)))
        else:
            print('커피 수량이 부족합니다.\n남은 커피수 : {}'.format(coffee))
    else:
        print('뭐 이딴돈으로 커피를 먹으러하냐 거지임??')
    print('남은 커피의 양은 {}개 입니다.'.format(coffee))

    if coffee == 0:
        print('품절입니다')
        break

# mylist1 = list(i for i in range(1,6))
# print(mylist1)
#
# mylist2 = list(10* i for i in range(1,6))
# print(mylist2)