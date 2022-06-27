from pythonoo.lab05.Controller import contorller
c = contorller()
def 新增():
    while True:

        c1 = int(input("請輸入編號"))
        c2 = str(input("請輸入名稱"))
        c3 = int(input("請輸入價格"))
        c.run(c1, c2, c3)
        y = input('是否繼續新增其他檔案?(y/n)')
        if y in 'nN':
            break

def 查詢():
    while True:

        f = int(input("請輸入查詢編號"))
        c.find(f)
        y = input('是否繼續查詢其他檔案?(y/n)')
        if y in 'nN':
            break

def 修改():
    while True:

        r1 = int(input("請輸想修改之編號"))
        r2 = str(input("請輸入商品名稱"))
        r3 = int(input("請輸入商品價格"))
        c.reset(r1,r2,r3)
        y = input('是否繼續修改其他檔案?(y/n)')
        if y in 'nN':
            break

def 刪除():
    while True:
        d1 = int(input("請輸想刪除之編號"))
        c.delete(d1)
        y = input('是否繼續刪除其他檔案?(y/n)')
        if y in 'nN':
            break
def 顯示():
    c.show_all()



#main
while True:
    option = input('請選擇功能(0.所有資料 1.新增 2.查詢 3.修改 4.刪除. q:結束):')
    if option == '1':
        新增()
    elif option == '2':
        查詢()
    elif option == '3':
        修改()
    elif option == '4':
        刪除()
    elif option == '0':
        顯示()
    elif option == 'q':
        print('結束')
        break
    else:
        print('輸入錯誤')