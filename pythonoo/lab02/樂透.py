import random

class Lotto:
    def __init__(self):
        self.numbers = list() #42號碼
        self.result = list() #結果 抽6個
    def 產生42號碼(self):
        for n in range(1, 43):
            self.numbers.append(n)

    def 抽出6個號碼(self):
        for x in range(6): #循環6次
            最前項 = 0
            最後項 = len(self.numbers) - 1
            i = random.randint(最前項, 最後項) #隨機決定第i項
            n = self.numbers.pop(i) #取除第 i 項
            self.result.append(n) #將 n 放入結果

    def 顯示結果(self):
        print(self.result)
#主流程
lo1 = Lotto() #建立物件(資料對象)自動執行__init__設定初值
lo1.產生42號碼()
lo1.抽出6個號碼()
lo1.顯示結果()

lo2 = Lotto() #建立物件(資料對象)自動執行__init__設定初值
lo2.產生42號碼()
lo2.抽出6個號碼()
lo2.顯示結果()