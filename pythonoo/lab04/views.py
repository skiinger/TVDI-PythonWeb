#資料輸出類別
class OutputView:
    def __init__(self):
        self.st = None

    def set(self, st):
        self.st = st

    def output(self):
        print(f'No.{self.st.id}')
        print(f'姓名:{self.st.name}')
        print(f'生日:{self.st.birthdate}')
