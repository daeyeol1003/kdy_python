print("===== <<< 리스트 >>> =====")

# 매우 중요
# 리스트는 대괄호[]로 감싼다
# 리스트는 추가, 수정, 삭제가 가능하다. 따라서 변경이 자주 일어날 경우 많이 사용

# 1. 리스트 출력
# 선언
list = [2,4,6,8,10]
print("list =>",list)

# 2. 리스트 추가 - append() => 리스트 맨끝에 추가됨
list.append(12)
print("list =>",list)

# 3. 리스트 생성하기
food = []  # 생성
food.append('갈비탕')
food.append('삼겹살')
food.append('뼈해장국')
food.append('라면')
food.append('설렁탕')
food.append('돈까스')
print(food)

# 4. 리스트 요소 접근하기(매우중요) => 리스트[인덱스]로 접근
# 인덱스는 앞에서부터 0부터 시작한다, 뒤에서부터는 -1 부터 시작
# 리스트명 = [요소1, 요소2, ...]
# 리스트안에서 어떠한 자료형도 포함시킬수 있다.

subject = ['국어','영어','수학']
print("subject[0] => ", subject[0])
print("subject[1] => ", subject[1])
print("subject[2] => ", subject[2])

# 5. 리스트 연산
list1 = [1,2,3] # 선언
print("list1 =>",list1) # list1 => [1,2,3]
print("합계 => ",list1[0]+list1[1]+list1[2])
print("뒤에서 첫번째 값 => ",list1[-1])

print("===== <<< 이중 리스트 >>> =====")
# 6. 이중리스트
list2 = [1,2,3,['x','y','z']]

print("1 출력 : ",list2[0])
print("2 출력 : ",list2[1])
print("3 출력 : ",list2[2])
print("x,y,z :",list2[-1])

print("x 출력 :",list2[-1][0])
print("y 출력 :",list2[3][1])
print("z 출력 :",list2[3][2])




