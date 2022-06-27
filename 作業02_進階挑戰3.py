def 顧客():
    while True:
        name = input('請輸入姓名')
        if len(name) < 2:
            print('姓名至少輸入兩個字')
        else:
            break
    return name


def 樂透():
    while True:
        lotto =input('請輸入六個號碼，用空格隔開')
        data = lotto.split()
        if len(data) != 6:
            print('請輸入6組號碼')
        elif len (set(data)) != 6:
            print('號碼不可重複!')
        else:
            break
    return data

def 儲存(na, da):
    result = ''
    result += na
    result += '\n'
    for v in da:
        result += v
        result += '\n'
    with open('lotto.txt', 'a', encoding='UTF-8') as f:
        f.write(result)
        print('輸入成功!')

def 字典儲存():
    with open('lotto.txt', 'w+') as f:
        f.write('{')  # 这样子字典没有自动的大括号要自己加
        for key in dict:
            f.write('\n')
            f.writelines('"' + str(key) + '": ' + str(dict[key]))
        f.write('\n' + '}')

import json

#進階1
n = 顧客()
d = 樂透()
儲存(n, d)
print('連續輸入資料')
cn = list()
cn.append(n)
while len(cn) < 4 :
    newn = 顧客()
    if newn not in cn:
        cn.append(newn)
        nd = 樂透()
        儲存(newn, nd)
    else:
        print('顧客姓名重複，請重新輸入')

#進階2
print('-----查詢資料-------')
with open('lotto.txt', encoding='UTF-8') as f:
    count = 1
    name = ''
    list_lotto = list()
    name_dict = dict()
    for i in f:
        i = i.replace('\n', '')
        if count % 7 == 1:
            name = i
            list_lotto = []
        else:
            list_lotto.append(i)
        count += 1
        name_dict[name] = list_lotto

print(name_dict)

while True:
    key = input('查詢名稱:')
    if key not in name_dict:
        print('輸入名稱不存在!')
    else:
        print(f'客戶 {key} 的樂透號碼為{name_dict[key]}')
    y = input('請問是否繼續查詢?(Y/N):')
    if y in 'Nn':
        break
print('輸入完成')
#挑戰3
while True:
    old_name = input('請輸入原本姓名')
    if old_name not in name_dict:
        print('此客戶並不存在')
    else:
        del name_dict[old_name]
        break
print('請輸入更新資料')
new_name = 顧客()
new_lotto = 樂透()
name_dict[new_name] =new_lotto
dict = name_dict
字典儲存()
print(f'資料更新完成，您的新的名稱為{new_name}，新的樂透號碼為{name_dict[new_name]}')





