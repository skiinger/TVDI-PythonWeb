#串列當資料庫
from pythonoo.lab05.models import Prodcut, Database

db = Database()

p1 = Prodcut()
p1.set(1, 'Apple', 100)
db.append(p1) #第0項

p2 = Prodcut()
p2.set(2, 'Banana', 200)
db.append(p2) #第1項

print('--所有資料--')
db.show()

print('--查詢 id:1--')
db.finding(1)

print('--修改 id:1--')
db.reset(1, 'New Apple', 350)
db.show()

print('--刪除資料 id:1--')
db.delete_p(1)
db.show()


