import random
class Lotto:
    def __init__(self):
        self.numbers = list()
        self.sixnb  = list()
    def 樂透列表(self):
        for i in range(1,43):
            self.numbers.append(i)
    def 抽號碼(self):
        for i in range(6):
            fist = 0
            list = len(self.numbers) - 1
            x = random.randint(fist, list)
            n = self.numbers.pop(x)
            self.sixnb.append(n)
    def 顯示(self):
        print(self.sixnb)

lo1 = Lotto()
lo1.樂透列表()
lo1.抽號碼()
lo1.顯示()