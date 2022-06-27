#設計類別(將函數與變數打包)命名慣例 第一個字大寫
class Student:
    #建構子 constructor 初值設定 規定命名為 __init__
    def __init__(self):
        self.name = None
        self.eng = None
        self.math = None
    def 修改值(self, name=None, eng=None, math=None):
        self.name = name
        self.eng = eng
        self.math = math
    def 總分(self):
        tot = None #區域變數 tot
        if self.eng is not None and self.math is not None:
            tot = self.eng + self.math
    def 顯示(self):
        tot = self.總分() #區域變數 tot
        print(self.name, self.eng, self.math, tot)

#主流程
st1 = Student() #Student()建立物件(資料對象)自動執行 __init__初值設定
st1.顯示()
st1.修改值('tom', 100, 99)
st1.顯示()

st2 = Student() #Student()建立物件(資料對象)自動執行 __init__初值設定
st2.顯示()
st2.修改值(math=80,eng=85,name='Amy')
st2.顯示()