def 初值(st): #區域變數 st
    name = None
    eng = None
    math = None
    st.append(name) #append是list函數
    st.append(eng)
    st.append(math)

def 修改值(st):
    name ='Tom'
    eng = 100
    math = 99
    st[0] = name
    st[1] = eng
    st[2] = math

def 總分(st):
    name = st[0]
    eng = st[1]
    math = st[2]
    #簡化寫法
    #name, eng, math = st
    tot = None
    if eng is not None and math is not None:
        tot = eng + math
    return tot

def 顯示(st):
    name = st[0]
    eng = st[1]
    math = st[2]
    tot = 總分(st)
    print(name, eng, math, tot)
#主流成
st = list() #全域變數st
初值(st) #全域變數st傳送到區域變數st(複製)
顯示(st)
修改值(st)
顯示(st)
