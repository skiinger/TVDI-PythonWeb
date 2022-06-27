from pythonoo.lab05.views import OutputView

v = OutputView()

while True:
    option = input('請選擇功能(0.所有資料 1.新增 2.查詢 3.修改 4.刪除. q:結束):')
    if option == '1':
        v.新增()
    elif option == '2':
        v.查詢()
    elif option == '3':
        v.修改()
    elif option == '4':
        v.刪除()
    elif option == '0':
        v.顯示()
    elif option == 'q':
        print('結束')
        break
    else:
        print('輸入錯誤')