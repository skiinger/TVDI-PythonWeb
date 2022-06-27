

#準備零件
from pythonoo.lab04.models import Date, Student

d = Date()
d.set(2000,1,1)#組裝3零件 2000 1 1

#準備零件
st = Student()
st.set(1, 'Tom', d) #組裝3零件
print(st)