from pythonoo.lab05.models import Prodcut, Database

db = Database()  #引入資料庫

class contorller:
    def __init__(self):
        pass

#新增檔案
    def run(self, no, name, cost):
        p = Prodcut()
        p.set(no, name, cost)
        db.append(p)
        db.show()

#查詢檔案
    def find(self,x):
        db.finding(x)

#修改檔案
    def reset(self,no,name,cost):
        db.reset(no, name, cost)
        db.show()

#刪除檔案
    def delete(self,x):
        db.delete_p(x)
        db.show()

#顯示檔案
    def show_all(self):
        db.show()
