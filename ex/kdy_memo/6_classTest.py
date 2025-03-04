class Calculate:
    def __init__(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return '더하기 : %d' %result

    def sub(self):
        result = self.first - self.second
        return '빼기 : %d' %result

    def mul(self):
        result = self.first *self.second
        return '곱하기 : %d' %result

    def div(self):
        if self.second == 0:
            self.second = 5
        result = self.first / self.second
        return '나누기 : %.3f'%result
num1 = int(input('첫번째 숫자를 입력하세요 :'))
num2 = int(input('두번째 숫자를 입력하세요 :'))
calc = Calculate(num1,num2)

print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())










