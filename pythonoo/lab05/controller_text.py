from pythonoo.lab05.Controller import contorller

#增加
c = contorller()
c1 = int(input("請輸入編號"))
c2 = str(input("請輸入名稱"))
c3 = int(input("請輸入價格"))
c.run(c1, c2, c3)

#查詢
f = int(input("請輸入查詢編號"))
c.find(f)

#修改
r1 = int(input("請輸想修改之編號"))
r2 = str(input("請輸入商品名稱"))
r3 = int(input("請輸入商品價格"))
c.reset(r1,r2,r3)

#刪除
d1 = int(input("請輸想刪除之編號"))
c.delete(d1)
