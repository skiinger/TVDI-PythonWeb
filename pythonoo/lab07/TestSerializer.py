from pythonoo.lab07.models import Product
from pythonoo.lab07.serialzers import Serializer

p1 = Product(1, 'Apple', 100)
Product.objects.save(p1)
p2 = Product(2, 'Banana', 200)
Product.objects.save(p2)

#序列化 Json
ser = Serializer()
s = ser.serialize(Product.objects.all())
print(s)