#Lab04 MVC(Model-View-Controller)

# Model 資料類別
class Date:
    #建構子 初值設定
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None
    def set (self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    #字串方法 method (類別裡面的函數稱為方法)
    def __str__(self):
        # return 'hahahahahaha'
        return f'{self.year}.{self.month}.{self.day}'

class Student:
    def __init__(self):
        self.id = None
        self.name = None
        self.birthdate = None

    def set(self, id, name, birthdate):
        self.id = id
        self.name = name
        # self.birthdate = birthdate
        self.birthdate = Date() #建立物件
        self.birthdate.year = birthdate.year
        self.birthdate.month = birthdate.month
        self.birthdate.day = birthdate.day

    def __str__(self):
        return f'{self.id} {self.name} {self.birthdate}'