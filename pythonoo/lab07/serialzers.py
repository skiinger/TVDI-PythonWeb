#序列化類別
class Serializer:
    def __init__(self):
        pass

    #所有產品資料
    def serialize(self, all):
        data =list() #list 相當於 JSON array
        for p in all:
            #將產品放到字典 dict 相當於 JSON object
            d = {'id':p.id, 'name':p.name, 'price':p.price}
            data.append(d) #將產品字典放到串列
        import json
        s = json.dumps(data) #data 轉換 json 字串
        return s