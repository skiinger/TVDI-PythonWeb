
#控制
from pythonoo.lab04.models import Date, Student
from pythonoo.lab04.views import OutputView


class Controller:
    def __init__(self):
        pass

    def run(self):
        #準備零件
        d = Date()
        d.set(2000,1,1) #組裝3零件 2000 1 1
        d2 = Date()
        d2.set(1986,3,18)

        # 準備零件
        st1 = Student()
        st1.set(1, 'Tom', d) #組裝3零件
        st2 = Student()
        st2.set(2,'rock', d2)

        #準備零件
        ov = OutputView()
        ov.set(st1)
        ov.output()
        ov.set(st2)
        ov.output()
