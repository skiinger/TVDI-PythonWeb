from lab04.models import Date, Student
from lab04.views import OutputView

#準備零件
d = Date()
d.set(2000,1,1)  #組裝3零件 2000 1 1

#準備零件
st1 = Student()
st1.set(1, 'Tom', d) #組裝3零件

#準備零件
ov = OutputView()
ov.set(st1)
ov.output()