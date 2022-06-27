class Student:
    def __init__(self):
        self.name = None
        self.eng = None
        self.math = None
    def 修改(self, name=None, eng=None, math=None):
        self.name = name
        self.eng = eng
        self.math = math
    def 總分(self):
        tot = None
        if self.eng is not None and self.math is not  None:
            tot = self.eng + self.math
    def 顯示(self):
        tot = self.總分()
        print(self.name, self.eng, self.math, tot)

st1 = Student()
st1.顯示()
st1.修改('Tom',80,90)
st1.顯示()