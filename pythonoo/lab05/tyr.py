# import csv
# # 二維表格
# table = [['班級', '學號', '成績'], ['資工一', '109590001', 90], ['資工一', '109590002', 85]]
# with open('output.csv', 'w', newline='',encoding="utf-8") as csvfile:
#     er = csv.writer(csvfile)
#     er.writerows(table) # 寫入二維表格
import csv


x = '1','an','8'
with open('Prodcut.csv', 'w+', newline='') as Prodcut_file:
    writer = csv.writer(Prodcut_file)
    print(x)
    writer.writerow(x)
