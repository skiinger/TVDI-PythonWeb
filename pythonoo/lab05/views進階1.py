from pythonoo.lab05.controller進階1 import contorller
c = contorller()

class OutputView:
    def __init__(self):
        pass

    def 新增(self):
        while True:
            c1 = int(input("請輸入編號"))
            c2 = str(input("請輸入名稱"))
            c3 = int(input("請輸入價格"))
            c.run(c1, c2, c3)
            y = input('是否繼續新增其他檔案?(y/n)')
            if y in 'nN':
                break

    def 查詢(self):
        while True:
            f = int(input("請輸入查詢編號"))
            c.find(f)
            y = input('是否繼續查詢其他檔案?(y/n)')
            if y in 'nN':
                break

    def 修改(self):
        while True:
            r1 = int(input("請輸想修改之編號"))
            r2 = str(input("請輸入商品名稱"))
            r3 = int(input("請輸入商品價格"))
            c.reset(r1, r2, r3)
            y = input('是否繼續修改其他檔案?(y/n)')
            if y in 'nN':
                break

    def 刪除(self):
        while True:
            d1 = int(input("請輸想刪除之編號"))
            c.delete(d1)
            y = input('是否繼續刪除其他檔案?(y/n)')
            if y in 'nN':
                break

    def 顯示(self):
        c.show_all()

    def 儲存(self):
        c.save_all()

    def 讀取(self):
        c.read_all()