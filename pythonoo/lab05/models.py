#Model 資料類別

class Prodcut:
    def __init__(self):
        self.no = None
        self.name = None
        self.cost = None
    def set(self,no, name, cost):
        self.no = no
        self.name = name
        self.cost = cost
    def __str__(self):
        return f'{self.no} {self.name} {self.cost}'

class Database(list):
    def __init__(self):
        pass

    def add(self,p):     #增加產品
        self.append(p)

    def finding(self,no): #搜尋產品
        index = no -1
        print(self[index])

    def reset(self,no, name, cost):  #修改產品
        new_p = Prodcut()
        new_p.set(no, name, cost)
        index = no-1
        self[index] = new_p

    def delete_p(self,no):  #刪除產品
        index = no-1
        if self[index] is not None:
            self[index] = None
        else:
            print('刪除失敗 檔案不存在')

    def show(self): #顯示產品列表
        for p in self:
            print(p)












