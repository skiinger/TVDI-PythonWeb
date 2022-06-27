from pythonoo.lab05.models進階1 import Database, Prodcut
db = list
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

#儲存檔案
    def save_all(self):
        db.csv_w()

#讀取檔案
    def read_all(self):
        db.csv_r()










