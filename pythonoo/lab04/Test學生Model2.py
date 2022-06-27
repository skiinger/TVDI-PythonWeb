

#準備零件
from pythonoo.lab04.models import Date, Student

d = Date()
d.set(2000,1,1)

#準備零件
st1 = Student()
st1.set(1, 'Tom', d) #組裝3零件
print(st1) #如果有類別 __str__ 會自動呼叫

d2 = Date()
d2.set(1983,2,5)
st2 = Student()
st2.set(2, 'Amy', d2) #組裝3零件
print(st2)

print('----修改日期----')
st2.birthdate.year = 1998
st2.birthdate.month = 12
st2.birthdate.day = 26
print(st1)
print(st2)

print('----修改姓名----')
st1.name = 'Rocking'
print(st1)
print(st2)

